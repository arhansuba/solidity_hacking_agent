import sys
import os



# Add the parent directory of 'solidtyhackingagents' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from solidtyhackingagents.tools.auditing.automated_scanning import automated_scanning
from solidtyhackingagents.tools.auditing.code_cleanliness import check_code_cleanliness
from solidtyhackingagents.tools.auditing.initial_review import initial_review
from solidtyhackingagents.tools.auditing.report_generation import  run_retests as generate_report
from solidtyhackingagents.tools.auditing.retesting_verification import retest_verification
from solidtyhackingagents.tools.auditing.testing import comprehensive_testing
from solidtyhackingagents.tools.utils.logging_utils import setup_logger as setup_logging

# Setup logging
logger_name = 'solidtyhackingagents'
log_file = 'solidtyhackingagents.log'
logger = setup_logging(name=logger_name, log_file=log_file)

# Define agents
analyst = Agent(
    role="Vulnerability Analyst",
    goal="Identify and analyze vulnerabilities in smart contracts",
    backstory="Expert in smart contract security and vulnerability analysis.",
    allow_delegation=False,
)

simulator = Agent(
    role="Attack Simulator",
    goal="Simulate attacks and stress test smart contracts",
    backstory="Specialist in attack simulations and stress testing.",
    allow_delegation=False,
)

scanner = Agent(
    role="Automated Scanner",
    goal="Run automated tools to scan for vulnerabilities",
    backstory="Expert in using automated tools for vulnerability scanning.",
    allow_delegation=False,
)

code_reviewer = Agent(
    role="Code Cleanliness Reviewer",
    goal="Ensure code cleanliness and adherence to best practices",
    backstory="Experienced in maintaining high code quality.",
    allow_delegation=False,
)

initial_reviewer = Agent(
    role="Initial Reviewer",
    goal="Perform an initial review of the smart contract",
    backstory="Skilled in initial contract assessments.",
    allow_delegation=False,
)

issue_categorizer = Agent(
    role="Issue Categorizer",
    goal="Categorize identified issues for further action",
    backstory="Adept at categorizing and prioritizing security issues.",
    allow_delegation=False,
)

manual_reviewer = Agent(
    role="Manual Reviewer",
    goal="Conduct a detailed manual review of the contract",
    backstory="Experienced in manual code reviews.",
    allow_delegation=False,
)

security_monitor = Agent(
    role="Ongoing Security Monitor",
    goal="Monitor ongoing security status of the contract",
    backstory="Specialist in continuous security monitoring.",
    allow_delegation=False,
)

report_generator = Agent(
    role="Report Generator",
    goal="Generate comprehensive reports",
    backstory="Proficient in creating detailed and clear reports.",
    allow_delegation=False,
)

retester = Agent(
    role="Retester",
    goal="Verify fixes and retest vulnerabilities",
    backstory="Expert in verification and retesting processes.",
    allow_delegation=False,
)

tester = Agent(
    role="Tester",
    goal="Conduct comprehensive testing of the smart contract",
    backstory="Experienced in various testing methodologies.",
    allow_delegation=False,
)

# Define tasks
tasks = [
    Task(
        description="Initial review of the smart contract.",
        func=initial_review,
        expected_output="Initial review report.",
        agent=initial_reviewer
    ),
    Task(
        description="Automated scanning of the smart contract using Mythril and Slither.",
        func=automated_scanning,
        expected_output="Automated scanning report.",
        agent=scanner
    ),
    Task(
        description="Check code cleanliness of the smart contract.",
        func=check_code_cleanliness,
        expected_output="Code cleanliness report.",
        agent=code_reviewer
    ),
    Task(
        description="Manual review of the smart contract.",
        func=manual_reviewer,
        expected_output="Manual review report.",
        agent=manual_reviewer
    ),
    Task(
        description="Retest the smart contract for previously identified vulnerabilities.",
        func=retest_verification,
        expected_output="Retest verification report.",
        agent=retester
    ),
    Task(
        description="Comprehensive testing of the smart contract.",
        func=comprehensive_testing,
        expected_output="Comprehensive testing report.",
        agent=tester
    ),
    Task(
        description="Generate the final report.",
        func=generate_report,
        expected_output="Final report.",
        agent=report_generator
    ),
  
]

# Set up manager LLM
manager_llm = ChatOpenAI(model_name="gpt-4")

# Define manager agent
manager = Agent(
    role="Project Manager",
    goal="Oversee the project and ensure high-quality output.",
    backstory="Experienced in managing complex projects and coordinating teams.",
    allow_delegation=True,
    tools=[manager_llm]
)

# Instantiate crew with a custom manager
crew = Crew(
    agents=[analyst, simulator, scanner, code_reviewer, initial_reviewer, issue_categorizer, manual_reviewer, security_monitor, report_generator, retester, tester],
    tasks=tasks,
    manager_agent=manager,
    process=Process.hierarchical,
    manager_llm=manager_llm
)

# Start the crew's work
result = crew.kickoff()
logger.info(result)
