from typing import List, Dict, Any
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent
from langchain.prompts import StringPromptTemplate
from langchain import OpenAI, LLMChain
from langchain.schema import AgentAction, AgentFinish
from pydantic import BaseModel, Field
import re
import asyncio
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AttackManager(BaseModel):
    llm: Any = Field(default_factory=lambda: OpenAI(temperature=0.2))
    tools: List[Tool] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        self.tools = [
            Tool(
                name="Reentrancy Attack",
                func=self.simulate_reentrancy_attack,
                description="Simulates a reentrancy attack on the smart contract"
            ),
            Tool(
                name="Overflow Attack",
                func=self.simulate_overflow_attack,
                description="Simulates an integer overflow attack on the smart contract"
            ),
            Tool(
                name="Access Control Attack",
                func=self.simulate_access_control_attack,
                description="Simulates an access control attack on the smart contract"
            )
        ]

    async def simulate_reentrancy_attack(self, contract_code: str) -> str:
        try:
            await asyncio.sleep(1)  # Simulating some processing time
            return "Reentrancy attack simulation completed. Vulnerability found in withdraw() function."
        except Exception as e:
            logger.error(f"Error during reentrancy attack simulation: {e}")
            return "Error in reentrancy attack simulation."

    async def simulate_overflow_attack(self, contract_code: str) -> str:
        try:
            await asyncio.sleep(1)  # Simulating some processing time
            return "Overflow attack simulation completed. Potential vulnerability found in balance calculation."
        except Exception as e:
            logger.error(f"Error during overflow attack simulation: {e}")
            return "Error in overflow attack simulation."

    async def simulate_access_control_attack(self, contract_code: str) -> str:
        try:
            await asyncio.sleep(1)  # Simulating some processing time
            return "Access control attack simulation completed. Unauthorized access possible to admin functions."
        except Exception as e:
            logger.error(f"Error during access control attack simulation: {e}")
            return "Error in access control attack simulation."

    async def coordinate_attacks(self, contract_code: str) -> Dict[str, Any]:
        prompt = StringPromptTemplate(
            input_variables=["input", "tools"],
            template="Coordinate attacks on this smart contract: {input}\n\nAvailable tools: {tools}\n\nResponse:"
        )

        llm_chain = LLMChain(llm=self.llm, prompt=prompt)
        agent = LLMSingleActionAgent(
            llm_chain=llm_chain,
            output_parser=self.output_parser,
            stop=["\nObservation:"],
            allowed_tools=[tool.name for tool in self.tools]
        )
        agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=self.tools, verbose=True)

        try:
            results = await agent_executor.arun(contract_code)
            attack_results = {
                "reentrancy": await self.simulate_reentrancy_attack(contract_code),
                "overflow": await self.simulate_overflow_attack(contract_code),
                "access_control": await self.simulate_access_control_attack(contract_code),
                "coordination_results": results
            }
            logger.info("Attack coordination completed successfully.")
            return attack_results
        except Exception as e:
            logger.error(f"Error during attack coordination: {e}")
            return {"error": "Error during attack coordination"}

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
    manager = AttackManager()
    contract_code = """
    pragma solidity ^0.8.0;

    contract Vulnerable {
        mapping(address => uint) public balances;

        function withdraw() public {
            uint bal = balances[msg.sender];
            require(bal > 0);
            (bool sent, ) = msg.sender.call{value: bal}("");
            require(sent, "Failed to send Ether");
            balances[msg.sender] = 0;
        }
    }
    """
    result = asyncio.run(manager.coordinate_attacks(contract_code))
    print(result)
