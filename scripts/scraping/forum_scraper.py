import aiohttp
import asyncio
from bs4 import BeautifulSoup
from typing import List, Dict, Any
import logging
import os
from dotenv import load_dotenv
from urllib.parse import urljoin

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

ETHEREUM_FORUM_URL = 'https://ethereum.stackexchange.com'

class ForumScraper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def fetch_page(self, url: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    logger.error(f"Error fetching page {url}: {response.status}")
                    return ""

    async def fetch_topics(self, tag: str = 'solidity', pages: int = 5) -> List[Dict[str, Any]]:
        topics = []
        for page in range(1, pages + 1):
            url = f"{self.base_url}/questions/tagged/{tag}?tab=newest&page={page}"
            html = await self.fetch_page(url)
            if html:
                soup = BeautifulSoup(html, 'html.parser')
                question_summaries = soup.find_all('div', class_='question-summary')
                for summary in question_summaries:
                    topic = {
                        'title': summary.find('h3').text.strip(),
                        'url': urljoin(self.base_url, summary.find('h3').find('a')['href']),
                        'votes': int(summary.find('span', class_='vote-count-post').text),
                        'answers': int(summary.find('div', class_='status').find('strong').text),
                        'views': int(summary.find('div', class_='views').text.split()[0].replace(',', '')),
                    }
                    topics.append(topic)
            await asyncio.sleep(1)  # Respectful delay between requests
        return topics

    async def fetch_topic_details(self, url: str) -> Dict[str, Any]:
        html = await self.fetch_page(url)
        if not html:
            return {}

        soup = BeautifulSoup(html, 'html.parser')
        question = soup.find('div', class_='question')
        answers = soup.find_all('div', class_='answer')

        details = {
            'question': self.extract_post_details(question),
            'answers': [self.extract_post_details(answer) for answer in answers],
        }
        return details

    @staticmethod
    def extract_post_details(post_soup: BeautifulSoup) -> Dict[str, Any]:
        return {
            'body': post_soup.find('div', class_='post-text').get_text(),
            'code': [code.get_text() for code in post_soup.find_all('code')],
            'score': int(post_soup.find('span', class_='vote-count-post').text),
        }

async def main():
    scraper = ForumScraper(ETHEREUM_FORUM_URL)
    topics = await scraper.fetch_topics()
    logger.info(f"Fetched {len(topics)} Solidity topics")

    for topic in topics[:3]:  # Limit to 3 topics for demonstration
        details = await scraper.fetch_topic_details(topic['url'])
        logger.info(f"Fetched details for topic: {topic['title']}")
        logger.info(f"Question body length: {len(details['question']['body'])}")
        logger.info(f"Number of answers: {len(details['answers'])}")

if __name__ == "__main__":
    asyncio.run(main())