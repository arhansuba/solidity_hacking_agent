from crewai import Task

# Define a research task
research_task = Task(
    description='Identify new vulnerabilities in Solidity smart contracts',
    expected_output='Detailed report on new vulnerabilities with examples.'
)

# Define an audit task
audit_task = Task(
    description='Audit smart contracts for known vulnerabilities',
    expected_output='Audit report with identified vulnerabilities and recommendations.'
)

# Define an attack management task
attack_task = Task(
    description='Develop and execute attack strategies on test contracts',
    expected_output='Detailed report on attack effectiveness and vulnerabilities exploited.'
)

# Assign tasks to the crew
crew.tasks = [research_task, audit_task, attack_task]
