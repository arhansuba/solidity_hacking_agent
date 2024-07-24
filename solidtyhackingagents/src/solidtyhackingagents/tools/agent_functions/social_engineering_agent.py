from crewai import Agent, Tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from pydantic import BaseModel, Field

class PhishingSimulation(Tool):
    name = "Phishing Simulation"
    description = "Simulates phishing attacks to test user awareness."

    def _run(self, target_email: str) -> str:
        # Placeholder for phishing simulation logic
        # Generate a phishing email scenario
        phishing_email = f"""
        Subject: Urgent Account Verification Needed

        Dear User,

        We have detected unusual activity in your account. To ensure the security of your account, please click the link below to verify your account information immediately:

        [Verify Now]

        Failure to do so may result in your account being temporarily suspended.

        Regards,
        Security Team
        """
        return phishing_email

class TrainingModule(Tool):
    name = "Social Engineering Training Module"
    description = "Provides training on recognizing and avoiding social engineering attacks."

    def __init__(self, name: str, description: str, content: str):
        super().__init__(name=name, description=description)
        self.content = content

    def _run(self, *args, **kwargs) -> str:
        return self.content

class SocialEngineeringAgent(Agent):
    def __init__(self):
        llm = OpenAI(temperature=0.7)

        phishing_simulation = PhishingSimulation()
        training_module = TrainingModule(
            name="Social Engineering Training Module",
            description="Provides training on recognizing and avoiding social engineering attacks.",
            content="Welcome to the social engineering training module. In this training, you will learn about common social engineering tactics such as phishing, pretexting, and baiting. Understanding these tactics will help you recognize and avoid potential attacks."
        )

        super().__init__(
            name="Social Engineering Agent",
            role="Social Engineering Specialist",
            goal="Simulate and train users on social engineering attacks.",
            backstory="An expert in social engineering, focused on simulating attacks and training individuals to recognize and defend against social engineering tactics.",
            verbose=True,
            llm=llm,
            tools=[phishing_simulation, training_module]
        )

    def simulate_phishing(self, target_email: str) -> str:
        # Simulate a phishing attack
        phishing_email = self.execute_tool("Phishing Simulation", target_email)
        return phishing_email

    def provide_training(self) -> str:
        # Provide training content on social engineering
        training_content = self.execute_tool("Social Engineering Training Module")
        return training_content

    def execute_tool(self, tool_name: str, *args) -> str:
        tool = next((t for t in self.tools if t.name == tool_name), None)
        if tool is None:
            raise ValueError(f"Tool '{tool_name}' not found.")
        return tool._run(*args)

if __name__ == "__main__":
    social_engineering_agent = SocialEngineeringAgent()
    
    # Simulate a phishing attack
    target_email = "user@example.com"
    phishing_email = social_engineering_agent.simulate_phishing(target_email)
    print("Phishing Email Simulation:")
    print(phishing_email)
    
    # Provide training on social engineering
    training_content = social_engineering_agent.provide_training()
    print("\nTraining Content:")
    print(training_content)
