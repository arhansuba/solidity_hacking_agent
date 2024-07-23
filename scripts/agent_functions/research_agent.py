from crewai import Agent

# Define research agent
research_agent = Agent(
    role='Researcher',
    goal='Conduct in-depth research on Solidity vulnerabilities',
    backstory='An expert in Solidity vulnerabilities and smart contract exploits.',
    tools=[],
    verbose=True,
    max_rpm=None,
    max_iter=25,
    allow_delegation=True
)

# Define audit agent
audit_agent = Agent(
    role='Auditor',
    goal='Audit smart contracts for security issues',
    backstory='A seasoned auditor specializing in smart contract security.',
    tools=['Tool1', 'Tool2', 'Tool3'],
    verbose=True,
    max_rpm=None,
    max_iter=25,
    allow_delegation=True
)

# Define attack manager agent
attack_manager = Agent(
    role='Attack Manager',
    goal='Coordinate and manage attack strategies',
    backstory='An expert strategist for managing and executing attack methods.',
    tools=[],
    verbose=True,
    max_rpm=None,
    max_iter=25,
    allow_delegation=True
)
from typing import List, Dict, Any
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, LLMChain
from langchain.schema import AgentAction, AgentFinish
from pydantic import BaseModel, Field
import requests
from bs4 import BeautifulSoup
import re

class ResearchAgent(BaseModel):
    llm: Any = Field(default_factory=lambda: OpenAI(temperature=0.3))
    tools: List[Tool] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        self.tools = [
            Tool(
                name="Search CVE Database",
                func=self.search_cve,
                description="Searches the CVE database for Solidity vulnerabilities"
            ),
            Tool(
                name="Fetch Latest Security Blogs",
                func=self.fetch_security_blogs,
                description="Fetches the latest blog posts about smart contract security"
            )
        ]

    def search_cve(self, query: str) -> str:
        # This is a mock function. In a real scenario, you'd interface with the actual CVE database.
        url = f"https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={query}+solidity"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            cves = soup.find_all('div', class_='row')
            return "\n".join([cve.text.strip() for cve in cves[:5]])
        return "Error fetching CVE data"

    def fetch_security_blogs(self, _: str) -> str:
        # This is a mock function. In a real scenario, you'd fetch from actual security blogs.
        blogs = [
            "ConsenSys: Top 10 Smart Contract Vulnerabilities",
            "OpenZeppelin: Common Smart Contract Vulnerabilities",
            "Trail of Bits: Smart Contract Security Checklist",
            "Ethereum Foundation: Smart Contract Best Practices",
            "Immunefi: Bug Bounty Writeups for Smart Contracts"
        ]
        return "\n".join(blogs)

    def research(self, topic: str) -> Dict[str, Any]:
        prompt = StringPromptTemplate(
            input_variables=["input", "tools"],
            template="Research this smart contract security topic: {input}\n\nAvailable tools: {tools}\n\nResponse:"
        )

        llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        agent = LLMSingleActionAgent(
            llm_chain=llm_chain,
            output_parser=self.output_parser,
            stop=["\nObservation:"],
            allowed_tools=[tool.name for tool in self.tools]
        )
        agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=self.tools, verbose=True)
        return agent_executor.run(topic)

    @staticmethod
    def output_parser(llm_output: str) -> AgentAction | AgentFinish:
        if "Final Answer:" in llm_output:
            return AgentFinish(
                return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                log=llm_output,
            )
        regex = r"Action: (.*?)[\n]*Action Input:[\s]*(.*)"
        match = re.search(regex, llm_output, re.DOTALL)
        if not match:
            raise ValueError(f"Could not parse LLM output: `{llm_output}`")
        action = match.group(1).strip()
        action_input = match.group(2)
        return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output)

if __name__ == "__main__":
    agent = ResearchAgent()
    result = agent.research("reentrancy vulnerabilities in smart contracts")
    print(result)