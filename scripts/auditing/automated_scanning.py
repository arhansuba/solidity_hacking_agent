# auditing/automated_scanning.py

import subprocess
from crewai import Agent, Task, Crew, Process

def run_mythril(contract_path):
    result = subprocess.run(["myth", "analyze", contract_path], capture_output=True, text=True)
    return result.stdout

def run_slither(contract_path):
    result = subprocess.run(["slither", contract_path], capture_output=True, text=True)
    return result.stdout

def automated_scanning(contract_path):
    mythril_agent = Agent(
        role="Mythril Scanner",
        goal="Scan the smart contract for vulnerabilities using Mythril",
        backstory="You are an expert in using Mythril for smart contract auditing",
        tools=[run_mythril]
    )

    slither_agent = Agent(
        role="Slither Scanner",
        goal="Scan the smart contract for vulnerabilities using Slither",
        backstory="You are an expert in using Slither for smart contract auditing",
        tools=[run_slither]
    )

    mythril_task = Task(
        description="Run Mythril on the smart contract",
        agent=mythril_agent
    )

    slither_task = Task(
        description="Run Slither on the smart contract",
        agent=slither_agent
    )

    crew = Crew(
        agents=[mythril_agent, slither_agent],
        tasks=[mythril_task, slither_task],
        process=Process.sequential
    )

    result = crew.kickoff()
    return result

# Usage
contract_path = "path/to/smart_contract.sol"
scan_results = automated_scanning(contract_path)
print(scan_results)