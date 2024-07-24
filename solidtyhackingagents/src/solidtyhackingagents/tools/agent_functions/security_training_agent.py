from crewai import Agent, Tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from pydantic import BaseModel, Field

class TrainingModule(Tool):
    def __init__(self, name: str, description: str, content: str):
        super().__init__(name=name, description=description)
        self.content = content

    def _run(self, *args, **kwargs) -> str:
        return self.content

class QuizGenerator(Tool):
    def __init__(self, name: str, description: str, generate_func):
        super().__init__(name=name, description=description)
        self.generate_func = generate_func

    def _run(self, topic: str) -> str:
        return self.generate_func(topic)

def generate_quiz(topic: str) -> str:
    # Placeholder for quiz generation logic
    return f"""
    Quiz on {topic}:
    1. What is the main vulnerability in smart contracts related to reentrancy?
    2. How can integer overflow be mitigated in Solidity contracts?
    3. Describe a common method to prevent access control issues in smart contracts.
    """

class SecurityTrainingAgent(Agent):
    def __init__(self):
        llm = OpenAI(temperature=0.7)

        security_module = TrainingModule(
            name="Security Training Module",
            description="Provides training content on smart contract security.",
            content="Welcome to the smart contract security training module. In this module, you'll learn about various vulnerabilities and best practices for securing smart contracts. Topics include reentrancy attacks, integer overflow, and access control."
        )
        
        quiz_generator = QuizGenerator(
            name="Quiz Generator",
            description="Generates quizzes based on the training content.",
            generate_func=generate_quiz
        )

        super().__init__(
            name="Security Training Agent",
            role="Training Facilitator",
            goal="Educate users on smart contract security.",
            backstory="An expert in smart contract security training, dedicated to helping users learn and understand smart contract vulnerabilities and best practices.",
            verbose=True,
            llm=llm,
            tools=[security_module, quiz_generator]
        )

    def deliver_training(self) -> str:
        # Provide the training content
        training_content = self.execute_tool("Security Training Module", "")
        return training_content

    def generate_quiz(self, topic: str) -> str:
        # Generate a quiz based on the training topic
        quiz = self.execute_tool("Quiz Generator", topic)
        return quiz

    def execute_tool(self, tool_name: str, *args) -> str:
        tool = next((t for t in self.tools if t.name == tool_name), None)
        if tool is None:
            raise ValueError(f"Tool '{tool_name}' not found.")
        return tool._run(*args)

if __name__ == "__main__":
    security_training_agent = SecurityTrainingAgent()
    
    # Deliver training content
    training_content = security_training_agent.deliver_training()
    print("Training Content:")
    print(training_content)
    
    # Generate a quiz on smart contract security
    quiz = security_training_agent.generate_quiz("Smart Contract Security")
    print("\nGenerated Quiz:")
    print(quiz)
