import aiohttp
import asyncio
from typing import List, Dict, Any
import logging
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

CYFRIN_API_KEY = os.getenv('CYFRIN_API_KEY')
CYFRIN_API_URL = 'https://api.cyfrin.io/v1'  # This is a hypothetical API URL

class CyfrinUpdraftIntegrator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    async def fetch_latest_vulnerabilities(self, days: int = 30) -> List[Dict[str, Any]]:
        url = f"{CYFRIN_API_URL}/vulnerabilities"
        params = {
            'from_date': (datetime.now() - timedelta(days=days)).isoformat()
        }

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['vulnerabilities']
                else:
                    logger.error(f"Error fetching vulnerabilities: {response.status}")
                    return []

    async def fetch_vulnerability_details(self, vulnerability_id: str) -> Dict[str, Any]:
        url = f"{CYFRIN_API_URL}/vulnerabilities/{vulnerability_id}"

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    logger.error(f"Error fetching vulnerability details for {vulnerability_id}: {response.status}")
                    return {}

    async def fetch_recommended_fixes(self, vulnerability_id: str) -> List[Dict[str, Any]]:
        url = f"{CYFRIN_API_URL}/vulnerabilities/{vulnerability_id}/fixes"

        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data['fixes']
                else:
                    logger.error(f"Error fetching recommended fixes for {vulnerability_id}: {response.status}")
                    return []

    async def submit_analysis(self, contract_code: str) -> Dict[str, Any]:
        url = f"{CYFRIN_API_URL}/analyze"
        payload = {