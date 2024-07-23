# stackoverflow_scraper.py

import requests
from bs4 import BeautifulSoup
from langchain.chains import OpenAIChain
from langchain.prompts import PromptTemplate

class StackOverflowScraper:
    def __init__(self, question_url: str, api_key: str):
        self.question_url = question_url
        self.api_key = api_key
        self.soup = None

    def fetch_question_data(self) -> None:
        """
        Fetch the content of the StackOverflow question page and parse it using BeautifulSoup.
        """
        response = requests.get(self.question_url)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, 'html.parser')
        print("StackOverflow data fetched and parsed.")

    def extract_question_data(self) -> dict:
        """
        Extract question and answer data from the parsed HTML content.
        """
        question_title = self.soup.find('h1', class_='question-title').text
        question_body = self.soup.find('div', class_='question-body').text
        answers = self.soup.find_all('div', class_='answer-body')
        answer_texts = [answer.text for answer in answers]
        return {'title': question_title, 'body': question_body, 'answers': answer_texts}

    def process_data_with_langchain(self, data: dict) -> dict:
        """
        Process the extracted data using LangChain for summarization or analysis.
        """
        prompt_template = PromptTemplate(template="Summarize the following question and its answers: {body}")
        chain = OpenAIChain(api_key=self.api_key, prompt_template=prompt_template)

        summary = chain.run(body=data['body'])
        return {'title': data['title'], 'summary': summary, 'answers': data['answers']}

# Example usage
if __name__ == "__main__":
    scraper = StackOverflowScraper('https://stackoverflow.com/questions/12345678', 'YOUR_LANGCHAIN_API_KEY')
    scraper.fetch_question_data()
    question_data = scraper.extract_question_data()
    processed_data = scraper.process_data_with_langchain(question_data)
    print(processed_data)
