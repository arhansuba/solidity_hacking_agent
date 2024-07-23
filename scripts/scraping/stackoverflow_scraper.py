import aiohttp
import asyncio
from bs4 import BeautifulSoup
from typing import List, Dict, Any
import logging
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

STACKOVERFLOW_API_KEY = os.getenv('STACKOVERFLOW_API_KEY')
STACKOVERFLOW_API_URL = 'https://api.stackexchange.com/2.3'

class StackOverflowScraper:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def fetch_questions(self, tag: str = 'solidity', from_date: timedelta = timedelta(days=30)) -> List[Dict[str, Any]]:
        url = f"{STACKOVERFLOW_API_URL}/questions"
        params = {
            'order': 'desc',
            'sort': 'activity',
            'tagged': tag,
            'site': 'stackoverflow',
            'key': self.api_key,
            'filter': 'withbody',
            'fromdate': int((datetime.now() - from_date).timestamp())
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['items']
                else:
                    logger.error(f"Error fetching questions: {response.status}")
                    return []

    async def fetch_answers(self, question_id: int) -> List[Dict[str, Any]]:
        url = f"{STACKOVERFLOW_API_URL}/questions/{question_id}/answers"
        params = {
            'order': 'desc',
            'sort': 'votes',
            'site': 'stackoverflow',
            'key': self.api_key,
            'filter': 'withbody'
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['items']
                else:
                    logger.error(f"Error fetching answers for question {question_id}: {response.status}")
                    return []

    @staticmethod
    def extract_code_snippets(html_content: str) -> List[str]:
        soup = BeautifulSoup(html_content, 'html.parser')
        code_blocks = soup.find_all('code')
        return [block.get_text() for block in code_blocks]

async def main():
    scraper = StackOverflowScraper(STACKOVERFLOW_API_KEY)
    questions = await scraper.fetch_questions()
    logger.info(f"Fetched {len(questions)} Solidity questions")

    for question in questions[:5]:  # Limit to 5 questions for demonstration
        answers = await scraper.fetch_answers(question['question_id'])
        logger.info(f"Fetched {len(answers)} answers for question {question['question_id']}")

        question_code = scraper.extract_code_snippets(question['body'])
        logger.info(f"Extracted {len(question_code)} code snippets from the question")

        for answer in answers:
            answer_code = scraper.extract_code_snippets(answer['body'])
            logger.info(f"Extracted {len(answer_code)} code snippets from answer {answer['answer_id']}")

if __name__ == "__main__":
    asyncio.run(main())