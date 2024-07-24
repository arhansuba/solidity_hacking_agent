from crewai import Agent, Tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from pydantic import BaseModel, Field

class RiskAnalyzer(Tool):
    def __init__(self, name: str, description: str, analyze_func):
        super().__init__(name=name, description=description)
        self.analyze_func = analyze_func

    def _run(self, contract_code: str) -> str:
        return self.analyze_func(contract_code)

class RiskReportGenerator(Tool):
    def __init__(self, name: str, description: str, generate_func):
        super().__init__(name=name, description=description)
        self.generate_func = generate_func

    def _run(self, risk_analysis: str) -> str:
        return self.generate_func(risk_analysis)

def analyze_risks(contract_code: str) -> str:
    # Placeholder for risk analysis logic
    return """
    Risk Analysis Report:
    1. Reentrancy Attack: High risk due to lack of checks-effects-interactions pattern.
    2. Integer Overflow: Potential risk in arithmetic operations.
    3. Access Control: Low risk as functions are protected with require statements.
    """

def generate_risk_report(risk_analysis: str) -> str:
    # Placeholder for generating a detailed risk report
    return f"""
    Detailed Risk Report:
    {risk_analysis}
    
    Recommendations:
    1. Implement checks-effects-interactions pattern to mitigate reentrancy attacks.
    2. Use SafeMath library to prevent integer overflow issues.
    3. Regularly audit access control mechanisms and test for potential weaknesses.
    """

class RiskAssessmentAgent(Agent):
    def __init__(self):
        llm = OpenAI(temperature=0.7)

        risk_analyzer = RiskAnalyzer(
            name="Risk Analyzer",
            description="Analyzes the smart contract for potential risks.",
            analyze_func=analyze_risks
        )
        
        risk_report_generator = RiskReportGenerator(
            name="Risk Report Generator",
            description="Generates a detailed risk report based on analysis.",
            generate_func=generate_risk_report
        )

        super().__init__(
            name="Risk Assessment Agent",
            role="Risk Assessor",
            goal="Evaluate and report on risks associated with smart contracts.",
            backstory="An expert in smart contract risk assessment, focusing on identifying and reporting potential risks to improve contract security.",
            verbose=True,
            llm=llm,
            tools=[risk_analyzer, risk_report_generator]
        )

    def assess_risks(self, contract_code: str) -> str:
        # Analyze risks associated with the smart contract
        risk_analysis = self.execute_tool("Risk Analyzer", contract_code)
        
        # Generate a detailed risk report based on the analysis
        risk_report = self.execute_tool("Risk Report Generator", risk_analysis)
        
        return risk_report

    def execute_tool(self, tool_name: str, input_data: str) -> str:
        tool = next((t for t in self.tools if t.name == tool_name), None)
        if tool is None:
            raise ValueError(f"Tool '{tool_name}' not found.")
        return tool._run(input_data)

if __name__ == "__main__":
    risk_assessment_agent = RiskAssessmentAgent()
    
    contract_code = """
    // Sample smart contract with potential risks
    contract RiskyContract {
        uint public balance;
        
        function withdraw(uint amount) public {
            require(balance >= amount);
            balance -= amount;
            payable(msg.sender).transfer(amount);
        }
    }
    """
    
    risk_report = risk_assessment_agent.assess_risks(contract_code)
    print("Risk Assessment Report:")
    print(risk_report)
