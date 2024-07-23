from crewai import Agent, Task, Crew, Process

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

# Define tasks
task1 = Task(
    description="Analyze smart contracts for known vulnerabilities using Slither and Mythril.",
    expected_output="Detailed vulnerability report.",
)

task2 = Task(
    description="Simulate attacks using Raven-Storm and hulk to test contract resilience.",
    expected_output="Attack simulation results and impact assessment.",
)

# Define manager agent
manager = Agent(
    role="Project Manager",
    goal="Oversee the project and ensure high-quality output.",
    backstory="Experienced in managing complex projects and coordinating teams.",
    allow_delegation=True,
)

# Instantiate crew with a custom manager
crew = Crew(
    agents=[analyst, simulator],
    tasks=[task1, task2],
    manager_agent=manager,
    process=Process.hierarchical,
)

# Start the crew's work
result = crew.kickoff()
