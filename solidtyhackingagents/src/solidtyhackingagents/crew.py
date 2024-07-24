# solidtyhackingagents/src/solidtyhackingagents/crew.py

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import yaml

# Import your custom tool
from solidtyhackingagents.tools.custom_tool import MyCustomTool

@CrewBase
class SolidtyhackingagentsCrew:
    """Crew for managing Solidity hacking agents"""

    agents_config_path = 'config/agents.yaml'
    tasks_config_path = 'config/tasks.yaml'

    def __init__(self):
        # Load agents and tasks configurations
        self.agents_config = self.load_config(self.agents_config_path)
        self.tasks_config = self.load_config(self.tasks_config_path)

    def load_config(self, path: str) -> dict:
        """Load configuration from a YAML file"""
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[MyCustomTool()],  # Use the custom tool
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher()
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            agent=self.reporting_analyst(),
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Create and return the Solidtyhackingagents crew"""
        return Crew(
            agents=[
                self.researcher(), 
                self.reporting_analyst()
            ],
            tasks=[
                self.research_task(), 
                self.reporting_task()
            ],
            process=Process.sequential,  # You can choose Process.hierarchical if preferred
            verbose=2
        )
