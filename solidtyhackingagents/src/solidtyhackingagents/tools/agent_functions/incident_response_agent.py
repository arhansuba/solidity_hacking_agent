from typing import List, Dict, Any
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, LLMChain
from langchain.schema import AgentAction, AgentFinish
from pydantic import BaseModel, Field
import re
from datetime import datetime

class IncidentResponseAgent(BaseModel):
    llm: Any = Field(default_factory=lambda: OpenAI(temperature=0.2))
    tools: List[Tool] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        self.tools = [
            Tool(
                name="Assess Incident",
                func=self.assess_incident,
                description="Assesses the severity and impact of the security incident"
            ),
            Tool(
                name="Containment Strategy",
                func=self.containment_strategy,
                description="Develops a strategy to contain the security incident"
            ),
            Tool(
                name="Recovery Plan",
                func=self.recovery_plan,
                description="Creates a plan to recover from the security incident"
            )
        ]

    def assess_incident(self, incident_details: str) -> str:
        # This is a placeholder for actual incident assessment logic
        severity = "High" if "funds stolen" in incident_details.lower() else "Medium"
        impact = "Significant financial loss" if "funds stolen" in incident_details.lower() else "Potential data breach"
        return f"Incident Severity: {severity}\nImpact: {impact}"

    def containment_strategy(self, incident_details: str) -> str:
        # This is a placeholder for actual containment strategy logic
        strategies = [
            "1. Immediately pause all contract functions to prevent further damage.",
            "2. Isolate affected smart contracts from the rest of the system.",
            "3. Monitor all related addresses for suspicious activities.",
            "4. Prepare for potential rollback or upgrade of the affected contracts."
        ]
        return "\n".join(strategies)

    def recovery_plan(self, incident_details: str) -> str:
        # This is a placeholder for actual recovery plan logic
        plan = [
            "1. Conduct a thorough post-mortem analysis to understand the root cause.",
            "2. Develop and deploy patches or upgrades to fix the vulnerability.",
            "3. Perform a comprehensive security audit of all related smart contracts.",
            "4. Implement additional monitoring and alert systems to prevent similar incidents.",
            "5. Communicate transparently with stakeholders about the incident and recovery efforts."
        ]
        return "\n".join(plan)

    def handle_incident(self, incident_details: str) -> Dict[str, Any]:
        prompt = StringPromptTemplate(
            input_variables=["input", "tools"],
            template="Handle this security incident in a smart contract: {input}\n\nAvailable tools: {tools}\n\nResponse:"
        )

        llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        agent = LLMSingleActionAgent(
            llm_chain=llm_chain,
            output_parser=self.output_parser,
            stop=["\nObservation:"],
            allowed_tools=[tool.name for tool in self.tools]
        )
        agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=self.tools, verbose=True)
        
        results = agent_executor.run(incident_details)
        return {
            "timestamp": datetime.now().isoformat(),
            "incident_details": incident_details,
            "assessment": self.assess_incident(incident_details),
            "containment_strategy": self.containment_strategy(incident_details),
            "recovery_plan": self.recovery_plan(incident_details),
            "overall_response": results
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
    responder = IncidentResponseAgent()
    incident_details = "A vulnerability in the withdraw function of our main contract has been exploited, resulting in the theft of 1000 ETH from user accounts."
    response = responder.handle_incident(incident_details)
    print(response)