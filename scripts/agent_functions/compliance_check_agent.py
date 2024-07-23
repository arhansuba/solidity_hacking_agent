from typing import List, Dict, Any
from crewai import Agent, Task
from langchain.tools import BaseTool
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.schema import AgentAction, AgentFinish
import re

class ComplianceScanner(BaseTool):
    name = "Compliance Scanner"
    description = "Scans smart contracts to ensure they meet compliance standards"

    def _run(self, contract_code: str) -> str:
        # Placeholder for compliance scanning logic
        # Replace with actual implementation
        return "Contract does not comply with the latest regulatory standards due to lack of reentrancy guard."

class SecurityBestPractices(BaseTool):
    name = "Security Best Practices"
    description = "Checks smart contracts against security best practices"

    def _run(self, contract_code: str) -> str:
        # Placeholder for checking security best practices
        # Replace with actual implementation
        return "Contract lacks proper access control mechanisms and does not implement fail-safes."

class ComplianceCheckAgent(Agent):
    def __init__(self):
        llm = OpenAI(temperature=0.5)
        compliance_scanner = ComplianceScanner()
        security_best_practices = SecurityBestPractices()

        super().__init__(
            name="Compliance Check Agent",
            role="Compliance and Security Specialist",
            goal="Ensure smart contracts meet compliance standards and security best practices",
            backstory="You are a specialist ensuring that smart contracts comply with regulatory standards and follow best security practices.",
            verbose=True,
            llm=llm,
            tools=[compliance_scanner, security_best_practices]
        )

    def check_compliance(self, contract_code: str) -> Dict[str, str]:
        try:
            compliance_results = self.run_tool("Compliance Scanner", contract_code)
            practices_results = self.run_tool("Security Best Practices", contract_code)

            return {
                "compliance": compliance_results,
                "security_best_practices": practices_results
            }
        except Exception as e:
            print(f"Error checking compliance: {e}")
            return {
                "compliance": "Error checking compliance",
                "security_best_practices": "Error checking security best practices"
            }

    def run_tool(self, tool_name: str, contract_code: str) -> str:
        tool = next((t for t in self.tools if t.name == tool_name), None)
        if not tool:
            raise ValueError(f"Tool {tool_name} not found")
        
        prompt = PromptTemplate(
            input_variables=["tool_name", "contract_code"],
            template="Use {tool_name} to analyze the following smart contract:\n\n{contract_code}"
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        return chain.run(tool_name=tool_name, contract_code=contract_code)

if __name__ == "__main__":
    # Example usage of the ComplianceCheckAgent
    compliance_agent = ComplianceCheckAgent()
    
    contract_code = """
    // Sample smart contract
    contract ExampleContract {
        uint public data;
        function setData(uint _data) public {
            data = _data;
        }
    }
    """
    compliance_results = compliance_agent.check_compliance(contract_code)
    print("Compliance Results:", compliance_results)
