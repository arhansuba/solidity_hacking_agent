from crewai import Agent, Task
from langchain.tools import BaseTool
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.graphs import NetworkxEntityGraph
import networkx as nx

class VulnerabilityScanner(BaseTool):
    name = "Vulnerability Scanner"
    description = "Scans smart contracts for potential vulnerabilities"

    def _run(self, contract_code: str) -> str:
        # Implement vulnerability scanning logic here
        # This is a placeholder and should be replaced with actual scanning code
        # Example output: List of identified vulnerabilities
        return "Potential reentrancy vulnerability found in function withdraw"

class ExploitGenerator(BaseTool):
    name = "Exploit Generator"
    description = "Generates potential exploits based on identified vulnerabilities"

    def _run(self, vulnerability: str) -> str:
        # Implement exploit generation logic here
        # This is a placeholder and should be replaced with actual exploit generation code
        # Example output: Exploit code for the given vulnerability
        return "Exploit code to trigger reentrancy vulnerability: [exploit code here]"

class BlackHatAgent(Agent):
    def __init__(self):
        llm = OpenAI(temperature=0.7)
        vulnerability_scanner = VulnerabilityScanner()
        exploit_generator = ExploitGenerator()

        super().__init__(
            name="Black Hat Agent",
            role="Ethical Hacker",
            goal="Identify and exploit smart contract vulnerabilities",
            backstory="You are an ethical hacker specializing in smart contract security. Your job is to find and demonstrate vulnerabilities in smart contracts to help improve their security.",
            verbose=True,
            llm=llm,
            tools=[vulnerability_scanner, exploit_generator]
        )

        self.attack_graph = NetworkxEntityGraph()

    def analyze_contract(self, contract_code: str):
        scan_task = Task(
            description="Scan the given smart contract for vulnerabilities",
            agent=self
        )
        scan_results = self.execute_task(scan_task, contract_code)
        vulnerabilities = self.parse_scan_results(scan_results)

        for vulnerability in vulnerabilities:
            exploit_task = Task(
                description=f"Generate an exploit for the {vulnerability}",
                agent=self
            )
            exploit = self.execute_task(exploit_task, vulnerability)

            self.attack_graph.add_edge("Contract", vulnerability)
            self.attack_graph.add_edge(vulnerability, exploit)

        return self.attack_graph

    def parse_scan_results(self, scan_results: str):
        # Parse the scan results to extract vulnerabilities
        # This is a simplified parser and should be replaced with more robust logic
        return [line.strip() for line in scan_results.split('.') if line.strip()]

    def execute_task(self, task: Task, input_data: str):
        prompt = PromptTemplate(
            input_variables=["task_description", "input_data"],
            template="Complete the following task: {task_description}\n\nInput data: {input_data}"
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        return chain.run(task_description=task.description, input_data=input_data)

if __name__ == "__main__":
    black_hat = BlackHatAgent()
    contract_code = """
    // Sample vulnerable smart contract
    contract VulnerableContract {
        mapping(address => uint) public balances;

        function withdraw() public {
            uint amount = balances[msg.sender];
            (bool success, ) = msg.sender.call{value: amount}("");
            require(success);
            balances[msg.sender] = 0;
        }
    }
    """
    attack_graph = black_hat.analyze_contract(contract_code)
    print(nx.info(attack_graph))
