from crewai import Agent
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import pickle

class AgentTrainingPipeline:
    def __init__(self, agent: Agent):
        self.agent = agent
        self.llm = OpenAI(temperature=0.7)
        self.training_data = []

    def set_training_data(self, data):
        self.training_data = data

    def train_agent(self):
        # Define a prompt template for training
        prompt_template = PromptTemplate(
            input_variables=["training_data"],
            template="Train the agent with the following data:\n{training_data}"
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)

        # Training the agent
        for data in self.training_data:
            print(f"Training with data: {data}")
            chain.run(training_data=data)

        # Save the trained agent
        self.save_agent()

    def save_agent(self):
        with open('trained_agent.pkl', 'wb') as f:
            pickle.dump(self.agent, f)
        print("Agent saved to 'trained_agent.pkl'")

if __name__ == "__main__":
    agent = Agent(
        name="Example Agent",
        role="Trainer",
        goal="Train on specific data",
        backstory="An agent trained to perform specific tasks.",
        tools=[],
        verbose=True
    )
    
    training_pipeline = AgentTrainingPipeline(agent=agent)
    training_pipeline.set_training_data([
        "Data example 1",
        "Data example 2",
        "Data example 3"
    ])
    training_pipeline.train_agent()
