from typing import List, Dict, Any
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, LLMChain
from langchain.schema import AgentAction, AgentFinish
from pydantic import BaseModel, Field
import re
import json

class ReportAgent(BaseModel):
    llm: Any = Field(default_factory=lambda: OpenAI(temperature=0.5))
    tools: List[Tool] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        self.tools = [
            Tool(
                name="Generate Executive Summary",
                func=self.generate_executive_summary,
                description="Generates an executive summary of the security audit findings"
            ),
            Tool(
                name="Generate Detailed Report",
                func=self.generate_detailed_report,
                description="Generates a detailed report of the security audit findings"
            ),
            Tool(
                name="Generate Recommendations",
                func=self.generate_recommendations,
                description="Generates recommendations based on the security audit findings"
            )
        ]

    def generate_executive_summary(self, findings: str) -> str:
        prompt = f"Generate a concise executive summary of the following security audit findings:\n\n{findings}"
        return self.llm(prompt)

    def generate_detailed_report(self, findings: str) -> str:
        prompt = f"Generate a detailed report of the following security audit findings, including technical details and potential impact:\n\n{findings}"
        return self.llm(prompt)

    def generate_recommendations(self, findings: str) -> str:
        prompt = f"Generate specific recommendations to address the following security audit findings:\n\n{findings}"
        return self.llm(prompt)

    def generate_report(self, audit_findings: Dict[str, Any]) -> Dict[str, Any]:
        prompt = StringPromptTemplate(
            input_variables=["input", "tools"],
            template="Generate a comprehensive security audit report based on these findings: {input}\n\nAvailable tools: {tools}\n\nResponse:"
        )

        llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        agent = LLMSingleActionAgent(
            llm_chain=llm_chain,
            output_parser=self.output_parser,
            stop=["\nObservation:"],
            allowed_tools=[tool.name for tool in self.tools]
        )
        agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=self.tools, verbose=True)
        
        findings_str = json.dumps(audit_findings, indent=2)
        report = agent_executor.run(findings_str)
        
        return {
            "executive_summary": self.generate_executive_summary(findings_str),
            "detailed_report": self.generate_detailed_report(findings_str),
            "recommendations": self.generate_recommendations(findings_str),
            "full_report": report
        }

    @staticmethod
    def output_parser(llm_output: str) -> AgentAction | AgentFinish:
        if "Final Answer:" in llm_output:
            return AgentFinish(
                return_values={"output": llm_output.split("Final Answer:")[-1].strip()},
                log=llm_output,
            )
        regex = r"Action: (.*?)[\n]*Action Input:[\s]*(.*)"
        match = re.search(regex, llm_output, re.DOTALL)
        if not match:
            raise ValueError(f"Could not parse LLM output: `{llm_output}`")
        action = match.group(1).strip()
        action_input = match.group(2)
        return AgentAction(tool=action, tool_input=action_input.strip(" ").strip('"'), log=llm_output)

if __name__ == "__main__":
    agent = ReportAgent()
    mock_findings = {
        "high_severity": [
            {"title": "Reentrancy Vulnerability", "description": "The contract is vulnerable to reentrancy attacks in the withdraw function."},
            {"title": "Unchecked External Call", "description": "The contract makes an external call without checking the return value."}
        ],
        "medium_severity": [
            {"title": "Timestamp Dependence", "description": "The contract uses block.timestamp as a source of randomness, which can be manipulated by miners."}
        ],
        "low_severity": [
            {"title": "Floating Pragma", "description": "The contract uses a floating pragma, which may lead to inconsistent behavior across different compiler versions."}
        ]
    }
    report = agent.generate_report(mock_findings)
    print(json.dumps(report, indent=2))