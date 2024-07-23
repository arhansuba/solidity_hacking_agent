# github_scraper.py

import requests
from langgraph import Graph
from langchain.chains import OpenAIChain
from langchain.prompts import PromptTemplate

class GitHubScraper:
    def __init__(self, repo_url: str, api_key: str):
        self.repo_url = repo_url
        self.api_key = api_key

    def fetch_repo_data(self) -> dict:
        """
        Fetch repository data from GitHub API.
        """
        headers = {'Authorization': f'token {self.api_key}'}
        issues_response = requests.get(f"{self.repo_url}/issues", headers=headers)
        pr_response = requests.get(f"{self.repo_url}/pulls", headers=headers)
        
        issues = issues_response.json()
        prs = pr_response.json()
        
        return {'issues': issues, 'pulls': prs}

    def analyze_data_with_langgraph(self, data: dict) -> dict:
        """
        Analyze the fetched data using LangGraph.
        """
        graph = Graph()
        for issue in data['issues']:
            graph.add_node(issue['title'], issue['body'])
        
        for pr in data['pulls']:
            graph.add_edge(pr['title'], pr['body'])
        
        # Process and analyze the graph
        analysis_result = graph.analyze()
        return analysis_result

# Example usage
if __name__ == "__main__":
    scraper = GitHubScraper('https://api.github.com/repos/owner/repo', 'YOUR_GITHUB_API_KEY')
    data = scraper.fetch_repo_data()
    analysis_result = scraper.analyze_data_with_langgraph(data)
    print(analysis_result)
