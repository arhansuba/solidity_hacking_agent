from crewai import Crew, Process

# Define a hierarchical crew with a manager
crew = Crew(
    agents=[research_agent, audit_agent, attack_manager],
    tasks=[/* List of tasks */],
    manager_agent=attack_manager,
    process=Process.hierarchical,
    memory=True
)
