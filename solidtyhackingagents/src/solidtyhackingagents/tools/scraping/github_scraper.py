import asyncio
import aiohttp
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from typing import List, Dict, Any
import logging
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_API_URL = 'https://api.github.com/graphql'

class GitHubScraper:
    def __init__(self, token: str):
        self.token = token
        self.transport = AIOHTTPTransport(url=GITHUB_API_URL, headers={'Authorization': f'Bearer {self.token}'})
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    async def fetch_solidity_repos(self, stars: int = 100, last_push: timedelta = timedelta(days=30)) -> List[Dict[str, Any]]:
        query = gql('''
        query ($queryString: String!, $cursor: String) {
          search(query: $queryString, type: REPOSITORY, first: 100, after: $cursor) {
            pageInfo {
              hasNextPage
              endCursor
            }
            nodes {
              ... on Repository {
                nameWithOwner
                url
                description
                stargazerCount
                forks {
                  totalCount
                }
                updatedAt
              }
            }
          }
        }
        ''')

        variables = {
            'queryString': f'language:Solidity stars:>{stars} pushed:>{(datetime.now() - last_push).date().isoformat()}',
            'cursor': None
        }

        repos = []
        while True:
            try:
                result = await self.client.execute_async(query, variable_values=variables)
                repos.extend(result['search']['nodes'])
                if not result['search']['pageInfo']['hasNextPage']:
                    break
                variables['cursor'] = result['search']['pageInfo']['endCursor']
            except Exception as e:
                logger.error(f"Error fetching repositories: {str(e)}")
                break

        return repos

    async def fetch_repo_contents(self, repo: str) -> List[Dict[str, Any]]:
        query = gql('''
        query ($owner: String!, $name: String!) {
          repository(owner: $owner, name: $name) {
            object(expression: "HEAD:") {
              ... on Tree {
                entries {
                  name
                  type
                  object {
                    ... on Blob {
                      text
                    }
                  }
                }
              }
            }
          }
        }
        ''')

        owner, name = repo.split('/')
        variables = {'owner': owner, 'name': name}

        try:
            result = await self.client.execute_async(query, variable_values=variables)
            return result['repository']['object']['entries']
        except Exception as e:
            logger.error(f"Error fetching repository contents for {repo}: {str(e)}")
            return []

async def main():
    scraper = GitHubScraper(GITHUB_TOKEN)
    repos = await scraper.fetch_solidity_repos()
    logger.info(f"Fetched {len(repos)} Solidity repositories")

    for repo in repos[:5]:  # Limit to 5 repos for demonstration
        contents = await scraper.fetch_repo_contents(repo['nameWithOwner'])
        logger.info(f"Fetched {len(contents)} files from {repo['nameWithOwner']}")

if __name__ == "__main__":
    asyncio.run(main())