from crewai import Agent, Tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from pydantic import BaseModel, Field
import json

class ThreatFeedIntegration(Tool):
    name = "Threat Feed Integration"
    description = "Integrates with threat intelligence feeds to gather data on emerging threats."

    def _run(self) -> str:
        # Placeholder for threat feed integration
        # Example output: JSON formatted threat data
        threat_data = {
            "threats": [
                {
                    "type": "Phishing",
                    "description": "New phishing campaign targeting financial institutions.",
                    "source": "ThreatFeed A"
                },
                {
                    "type": "Ransomware",
                    "description": "Ransomware variant X spreading rapidly across Europe.",
                    "source": "ThreatFeed B"
                }
            ]
        }
        return json.dumps(threat_data, indent=2)

class ThreatAnalysis(Tool):
    name = "Threat Analysis"
    description = "Analyzes gathered threat intelligence to identify patterns and potential impacts."

    def _run(self, threat_data: str) -> str:
        # Placeholder for threat analysis logic
        # Analyze threat data and provide insights
        # Example output: Summary of threats
        threat_info = json.loads(threat_data)
        summary = "Summary of Threats:\n"
        for threat in threat_info["threats"]:
            summary += f"Type: {threat['type']}, Description: {threat['description']}, Source: {threat['source']}\n"
        return summary

class ThreatIntelligenceAgent(Agent):
    def __init__(self):
        llm = OpenAI(temperature=0.7)

        threat_feed_integration = ThreatFeedIntegration()
        threat_analysis = ThreatAnalysis()

        super().__init__(
            name="Threat Intelligence Agent",
            role="Threat Intelligence Specialist",
            goal="Gather, analyze, and interpret threat intelligence to provide actionable insights.",
            backstory="A threat intelligence expert focused on identifying emerging threats and providing insights to improve security posture.",
            verbose=True,
            llm=llm,
            tools=[threat_feed_integration, threat_analysis]
        )

    def gather_threat_data(self) -> str:
        # Gather threat data from integrated feeds
        threat_data = self.execute_tool("Threat Feed Integration")
        return threat_data

    def analyze_threats(self, threat_data: str) -> str:
        # Analyze the gathered threat data
        analysis_summary = self.execute_tool("Threat Analysis", threat_data)
        return analysis_summary

    def execute_tool(self, tool_name: str, *args) -> str:
        tool = next((t for t in self.tools if t.name == tool_name), None)
        if tool is None:
            raise ValueError(f"Tool '{tool_name}' not found.")
        return tool._run(*args)

if __name__ == "__main__":
    threat_intelligence_agent = ThreatIntelligenceAgent()
    
    # Gather threat data
    threat_data = threat_intelligence_agent.gather_threat_data()
    print("Threat Data:")
    print(threat_data)
    
    # Analyze threats
    analysis_summary = threat_intelligence_agent.analyze_threats(threat_data)
    print("\nThreat Analysis Summary:")
    print(analysis_summary)
