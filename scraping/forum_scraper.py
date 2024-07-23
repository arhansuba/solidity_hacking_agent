# forum_scraper.py

import requests
from bs4 import BeautifulSoup
from langchain.chains import OpenAIChain
from langchain.prompts import PromptTemplate
from langgraph import Graph

class ForumScraper:
    def __init__(self, forum_url: str, api_key: str):
        self.forum_url = forum_url
        self.api_key = api_key
        self.soup = None

    def fetch_forum_data(self) -> None:
        """
        Fetch the content of the forum page and parse it using BeautifulSoup.
        """
        response = requests.get(self.forum_url)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, 'html.parser')
        print("Forum data fetched and parsed.")

    def extract_post_data(self) -> list:
        """
        Extract post data from the parsed HTML content.
        """
        posts = self.soup.find_all('div', class_='post-content')
        post_data = []
        for post in posts:
            title = post.find('h2').text
            content = post.find('p').text
            post_data.append({'title': title, 'content': content})
        return post_data

    def process_data_with_langchain(self, data: list) -> list:
        """
        Process the extracted data using LangChain for further analysis or summarization.
        """
        prompt_template = PromptTemplate(template="Summarize the following forum post: {content}")
        chain = OpenAIChain(api_key=self.api_key, prompt_template=prompt_template)

        processed_data = []
        for post in data:
            summary = chain.run(content=post['content'])
            processed_data.append({'title': post['title'], 'summary': summary})
        return processed_data

# Example usage
if __name__ == "__main__":
    scraper = ForumScraper('https://exampleforum.com', 'YOUR_LANGCHAIN_API_KEY')
    scraper.fetch_forum_data()
    posts = scraper.extract_post_data()
    summaries = scraper.process_data_with_langchain(posts)
    for summary in summaries:
        print(summary)
