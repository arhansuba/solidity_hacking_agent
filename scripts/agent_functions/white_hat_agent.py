from crewai import Agent, Task
from langchain.tools import BaseTool
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.graphs import NetworkxEntityGraph
import networkx as nx

class SecurityAuditor(BaseTool):
    name = "Security Auditor"
    description = "Conducts a comprehensive security audit of smart contracts"

    def _run(self, contract_code: str) -> str:
        # Implement security auditing logic here
        # This is a placeholder and should be replaced with actual auditing code
        return "Security audit completed. Found 2 high-risk vulnerabilities and 3 medium-risk issues."

class PatchGenerator(BaseTool):
    name = "Patch Generator"
    description = "Generates patches for identified vulnerabilities"

    def _run(self, vulnerability: str) -> str:
        # Implement patch generation logic here
        # This is a placeholder and should be replaced with actual patch generation code
        return "Patch for reentrancy vulnerability: [patch code here]"

class WhiteHatAgent(Agent):
    def __init__(self):
        llm = OpenAI(temperature=0.3)
        security_auditor = SecurityAuditor()
        patch_generator = PatchGenerator()

        super().__init__(
            name="White Hat Agent",
            role="Security Researcher",
            goal="Identify vulnerabilities and propose security improvements for smart contracts",
            backstory="You are a respected security researcher specializing in blockchain technology. Your mission is to make smart contracts more secure by identifying vulnerabilities and proposing fixes.",
            verbose=True,
            llm=llm,
            tools=[security_auditor, patch_generator]
        )

        self.security_graph = NetworkxEntityGraph()

    def audit_contract(self, contract_code: str):
        audit_task = Task(
            description="Conduct a comprehensive security audit of the given smart contract",
            agent=self
        )
        audit_results = self.execute_task(audit_task, contract_code)

        vulnerabilities = self.parse_audit_results(audit_results)

        for vulnerability in vulnerabilities:
            patch_task = Task(
                description=f"Generate a patch for the {vulnerability}",
                agent=self
            )
            patch = self.execute_task(patch_task, vulnerability)

            self.security_graph.add_edge("Contract", vulnerability)
            self.security_graph.add_edge(vulnerability, patch)

        return self.security_graph

    def parse_audit_results(self, audit_results: str):
        # This is a simplified parser and should be replaced with more robust logic
        return [line.strip() for line in audit_results.split('.') if line.strip()]

    def execute_task(self, task: Task, input_data: str):
        prompt = PromptTemplate(
            input_variables=["task_description", "input_data"],
            template="Complete the following task: {task_description}\n\nInput data: {input_data}"
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        return chain.run(task_description=task.description, input_data=input_data)

    def propose_improvements(self, attack_graph: NetworkxEntityGraph):
        improvement_task = Task(
            description="Analyze the attack graph and propose security improvements",
            agent=self
        )
        improvements = self.execute_task(improvement_task, nx.info(attack_graph))
        return improvements

if __name__ == "__main__":
    white_hat = WhiteHatAgent()
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
    security_graph = white_hat.audit_contract(contract_code)
    print(nx.info(security_graph))

    # Simulate receiving an attack graph from the Black Hat Agent
    attack_graph = NetworkxEntityGraph()
    attack_graph.add_edge("Contract", "Reentrancy Vulnerability")
    attack_graph.add_edge("Reentrancy Vulnerability", "Exploit Code")

    improvements = white_hat.propose_improvements(attack_graph)
    print("Proposed improvements:", improvements)
