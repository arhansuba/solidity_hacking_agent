import re
from typing import List, Dict, Any
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, LLMChain
from langchain.schema import AgentAction, AgentFinish
from pydantic import BaseModel, Field

class BasicErrorAgent(BaseModel):
    llm: Any = Field(default_factory=lambda: OpenAI(temperature=0))
    tools: List[Tool] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        self.tools = [
            Tool(
                name="Solidity Syntax Checker",
                func=self.check_solidity_syntax,
                description="Checks Solidity code for basic syntax errors"
            ),
            Tool(
                name="Common Vulnerability Detector",
                func=self.detect_common_vulnerabilities,
                description="Detects common Solidity vulnerabilities"
            )
        ]

    def check_solidity_syntax(self, code: str) -> str:
        # This is a simplified syntax checker. In a real-world scenario,
        # you'd use a more robust Solidity parser.
        errors = []
        lines = code.split('\n')
        for i, line in enumerate(lines):
            if '{' in line and '}' in line and '//' not in line:
                errors.append(f"Line {i+1}: Possible inline bracketing, consider splitting to multiple lines")
            if 'function' in line and ';' in line:
                errors.append(f"Line {i+1}: Function declaration should not end with a semicolon")
            if 'contract' in line and '{' not in line:
                errors.append(f"Line {i+1}: Contract declaration should be followed by an opening brace")
        return '\n'.join(errors) if errors else "No basic syntax errors detected."

    def detect_common_vulnerabilities(self, code: str) -> str:
        vulnerabilities = []
        if "tx.origin" in code:
            vulnerabilities.append("Potential use of tx.origin for authorization. Consider using msg.sender instead.")
        if "block.timestamp" in code:
            vulnerabilities.append("Use of block.timestamp. Be aware of possible miner manipulations.")
        if "assembly" in code:
            vulnerabilities.append("Use of assembly detected. Ensure it's necessary and well-audited.")
        if re.search(r"transfer\(.+\)", code):
            vulnerabilities.append("Use of transfer() detected. Consider using send() or call() for better gas handling.")
        return '\n'.join(vulnerabilities) if vulnerabilities else "No common vulnerabilities detected."

    def analyze(self, contract_code: str) -> Dict[str, Any]:
        prompt = StringPromptTemplate(
            input_variables=["input", "tools"],
            template="Analyze this Solidity contract for basic errors and vulnerabilities: {input}\n\nAvailable tools: {tools}\n\nResponse:"
        )

        llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        agent = LLMSingleActionAgent(
            llm_chain=llm_chain,
            output_parser=self.output_parser,
            stop=["\nObservation:"],
            allowed_tools=[tool.name for tool in self.tools]
        )
        agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=self.tools, verbose=True)
        return agent_executor.run(contract_code)

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
    agent = BasicErrorAgent()
    contract = """
    pragma solidity ^0.8.0;

    contract Vulnerable {
        function transfer(address payable _to) public payable {
            _to.transfer(msg.value);
        }

        function checkTimestamp() public view returns (bool) {
            return block.timestamp % 15 == 0;
        }
    }
    """
    result = agent.analyze(contract)
    print(result)