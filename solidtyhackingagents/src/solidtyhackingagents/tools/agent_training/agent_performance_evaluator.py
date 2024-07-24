from crewai import Agent
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import pickle

class AgentPerformanceEvaluator:
    def __init__(self, agent: Agent):
        self.agent = agent
        self.llm = OpenAI(temperature=0.7)
        self.metrics = []

    def set_metrics(self, metrics):
        self.metrics = metrics

    def evaluate_performance(self):
        # Define a prompt template for performance evaluation
        prompt_template = PromptTemplate(
            input_variables=["metrics"],
            template="Evaluate the agent's performance based on the following metrics:\n{metrics}"
        )
        chain = LLMChain(llm=self.llm, prompt=prompt_template)

        # Evaluate the agent
        performance_report = chain.run(metrics=self.metrics)
        print("Performance Report:")
        print(performance_report)

        # Save the performance report
        self.save_report(performance_report)

    def save_report(self, report: str):
        with open('performance_report.txt', 'w') as f:
            f.write(report)
        print("Performance report saved to 'performance_report.txt'")

if __name__ == "__main__":
    # Load a trained agent
    with open('trained_agent.pkl', 'rb') as f:
        trained_agent = pickle.load(f)
    
    evaluator = AgentPerformanceEvaluator(agent=trained_agent)
    evaluator.set_metrics([
        "Metric 1: Accuracy",
        "Metric 2: Response Time",
        "Metric 3: User Satisfaction"
    ])
    evaluator.evaluate_performance()
