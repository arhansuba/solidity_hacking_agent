from crewai import Agent, Tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from pydantic import BaseModel, Field
import json

class ForensicAnalysisTool(Tool):
    def __init__(self, name: str, description: str, analysis_func):
        super().__init__(name=name, description=description)
        self.analysis_func = analysis_func

    def _run(self, contract_code: str) -> str:
        return self.analysis_func(contract_code)

def analyze_attack_traces(contract_code: str) -> str:
    # Placeholder for forensic analysis of attack traces
    # Example output: Analysis report of attack traces
    return """
    Forensic Analysis Report:
    - Reentrancy attack detected in the withdraw function.
    - Suspected manipulation of state variables.
    - Unusual contract interactions observed.
    """

def assess_impact_of_vulnerabilities(contract_code: str) -> str:
    # Placeholder for assessing the impact of vulnerabilities
    # Example output: Impact assessment report
    return """
    Impact Assessment Report:
    - Reentrancy attack could lead to loss of funds.
    - Integer overflow may cause incorrect balance calculations.
    - Access control issues might allow unauthorized actions.
    """

def generate_forensic_report(analysis: str, impact: str) -> str:
    # Create a detailed forensic report
    prompt = PromptTemplate(
        input_variables=["analysis", "impact"],
        template="Generate a comprehensive forensic report based on the following analysis and impact assessment:\n\nAnalysis:\n{analysis}\n\nImpact Assessment:\n{impact}"
    )
    llm = OpenAI(temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(analysis=analysis, impact=impact)

class ForensicsAgent(Agent):
    def __init__(self):
        llm = OpenAI(temperature=0.7)
        
        attack_trace_tool = ForensicAnalysisTool(
            name="Attack Trace Analyzer",
            description="Analyzes traces of attacks in smart contracts.",
            analysis_func=analyze_attack_traces
        )
        
        impact_assessment_tool = ForensicAnalysisTool(
            name="Impact Assessor",
            description="Assesses the impact of vulnerabilities in smart contracts.",
            analysis_func=assess_impact_of_vulnerabilities
        )
        
        super().__init__(
            name="Forensics Agent",
            role="Forensic Analyst",
            goal="Perform forensic analysis on smart contracts to identify and assess attacks.",
            backstory="A forensic analyst specializing in smart contract security, focusing on tracing attacks and assessing their impact.",
            verbose=True,
            llm=llm,
            tools=[attack_trace_tool, impact_assessment_tool]
        )
    
    def perform_forensic_analysis(self, contract_code: str) -> str:
        # Perform forensic analysis and generate a report
        analysis = self.execute_tool("Attack Trace Analyzer", contract_code)
        impact = self.execute_tool("Impact Assessor", contract_code)
        report = generate_forensic_report(analysis, impact)
        return report

    def execute_tool(self, tool_name: str, input_data: str) -> str:
        tool = next((t for t in self.tools if t.name == tool_name), None)
        if tool is None:
            raise ValueError(f"Tool '{tool_name}' not found.")
        return tool._run(input_data)

if __name__ == "__main__":
    forensics_agent = ForensicsAgent()
    
    contract_code = """
    // Sample smart contract
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
    
    forensic_report = forensics_agent.perform_forensic_analysis(contract_code)
    print(forensic_report)
