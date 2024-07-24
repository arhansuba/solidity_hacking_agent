import subprocess
from crewai import Agent, Task, Crew, Process

# Define functions for scanning
def run_mythril(contract_path):
    """Run Mythril to analyze the smart contract for vulnerabilities."""
    result = subprocess.run(["myth", "analyze", contract_path], capture_output=True, text=True)
    return result.stdout

def run_slither(contract_path):
    """Run Slither to analyze the smart contract for vulnerabilities."""
    result = subprocess.run(["slither", contract_path], capture_output=True, text=True)
    return result.stdout

def automated_scanning(contract_path):
    """Perform automated scanning of the smart contract using Mythril and Slither."""
    
    # Create Mythril agent
    mythril_agent = Agent(
        role="Mythril Scanner",
        goal="Scan the smart contract for vulnerabilities using Mythril",
        backstory="Expert in using Mythril for smart contract auditing.",
        tools=[run_mythril]
    )

    # Create Slither agent
    slither_agent = Agent(
        role="Slither Scanner",
        goal="Scan the smart contract for vulnerabilities using Slither",
        backstory="Expert in using Slither for smart contract auditing.",
        tools=[run_slither]
    )

    # Define Mythril task
    mythril_task = Task(
        description="Run Mythril on the smart contract.",
        agent=mythril_agent,
        parameters={'contract_path': contract_path}
    )

    # Define Slither task
    slither_task = Task(
        description="Run Slither on the smart contract.",
        agent=slither_agent,
        parameters={'contract_path': contract_path}
    )

    # Create crew with sequential process
    crew = Crew(
        agents=[mythril_agent, slither_agent],
        tasks=[mythril_task, slither_task],
        process=Process.sequential
    )

    # Start the crew's work and get results
    result = crew.kickoff()
    return result

# Usage example
if __name__ == "__main__":
    contract_path = "/home/arhan/SolidityHackingAgent/MultiOwnable.sol"
    scan_results = automated_scanning(contract_path)
    print(scan_results)
