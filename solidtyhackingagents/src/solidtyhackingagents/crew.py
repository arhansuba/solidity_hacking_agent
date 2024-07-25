from crewai import Agent, Crew, Process, CrewBase, Task, agent, task

import yaml

# Import your custom tool
from solidtyhackingagents.tools.hacktool import ConcreteTool
from langchain_openai import ChatOpenAI
from solidtyhackingagents.tools.hacktool import attack_manager, audit_agent, exploit_generator_agent, knowledge_update_agent, basic_error_agent, behavioral_analysis_agent, black_hat_agent, compliance_check_agent, configure_crew, define_agent, disaster_recovery_agent, economic_attack_agent, forensics_agent, incident_response_agent, patch_management_agent, privacy_breach_agent, rapid_deployment_agent, report_agent, research_agent, risk_assessment_agent, security_training_agent, social_engineering_agent, threat_intelligence_agent, vulnerability_scanner_agent, white_hat_agent
from solidtyhackingagents.tools.hacktool import setup_logging

# Setup logging
logger = setup_logging()
@CrewBase
class SolidtyhackingagentsCrew:
    """Crew for managing Solidity hacking agents"""

    agents_config_path = 'config/agents.yaml'
    tasks_config_path = 'config/tasks.yaml'

    def __init__(self):
        # Load agents and tasks configurations
        self.agents_config = self.load_config(self.agents_config_path)
        self.tasks_config = self.load_config(self.tasks_config_path)

    def load_config(self, path: str) -> dict:
        """Load configuration from a YAML file"""
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[ConcreteTool()],  # Use ConcreteTool
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            tools=[ConcreteTool()],  # Use ConcreteTool if needed
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher()
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            agent=self.reporting_analyst(),
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Create and return the Solidtyhackingagents crew"""
        return Crew(
            agents=[
                self.researcher(), 
                self.reporting_analyst()
            ],
            tasks=[
                self.research_task(), 
                self.reporting_task()
            ],
            process=Process.sequential,  # You can choose Process.hierarchical if preferred
            verbose=2
        )
agents = {
    "attack_manager": Agent(
        role="Attack Manager",
        goal="Manage and oversee attack strategies.",
        backstory="Expert in attack strategies and management.",
        allow_delegation=False,
    ),
    "audit_agent": Agent(
        role="Audit Agent",
        goal="Conduct audits on smart contracts.",
        backstory="Specialist in performing comprehensive audits.",
        allow_delegation=False,
    ),
    "basic_error_agent": Agent(
        role="Basic Error Agent",
        goal="Identify and handle basic errors in smart contracts.",
        backstory="Experienced in spotting and resolving basic contract errors.",
        allow_delegation=False,
    ),
    "behavioral_analysis_agent": Agent(
        role="Behavioral Analysis Agent",
        goal="Analyze behavior and patterns of smart contracts.",
        backstory="Adept in behavioral analysis of smart contracts.",
        allow_delegation=False,
    ),
    "black_hat_agent": Agent(
        role="Black Hat Agent",
        goal="Simulate malicious attacks to test vulnerabilities.",
        backstory="Specializes in black hat techniques and testing.",
        allow_delegation=False,
    ),
    "compliance_check_agent": Agent(
        role="Compliance Check Agent",
        goal="Ensure compliance with relevant standards and regulations.",
        backstory="Expert in regulatory compliance and checks.",
        allow_delegation=False,
    ),
    "configure_crew": Agent(
        role="Crew Configurator",
        goal="Configure and manage crew settings and tasks.",
        backstory="Specialist in crew configuration and management.",
        allow_delegation=False,
    ),
    "define_agent": Agent(
        role="Agent Definition Specialist",
        goal="Define and specify agent roles and tasks.",
        backstory="Experienced in defining roles and responsibilities for agents.",
        allow_delegation=False,
    ),
    "disaster_recovery_agent": Agent(
        role="Disaster Recovery Agent",
        goal="Manage disaster recovery strategies and plans.",
        backstory="Expert in disaster recovery and contingency planning.",
        allow_delegation=False,
    ),
    "economic_attack_agent": Agent(
        role="Economic Attack Agent",
        goal="Analyze and simulate economic attacks on smart contracts.",
        backstory="Specializes in economic attack strategies and simulations.",
        allow_delegation=False,
    ),
    "exploit_generator_agent": Agent(
        role="Exploit Generator",
        goal="Generate and test new exploits for vulnerabilities.",
        backstory="Expert in creating and testing new exploits.",
        allow_delegation=False,
    ),
    "forensics_agent": Agent(
        role="Forensics Agent",
        goal="Conduct forensic analysis of contract breaches and incidents.",
        backstory="Specialist in forensic analysis and investigations.",
        allow_delegation=False,
    ),
    "incident_response_agent": Agent(
        role="Incident Response Agent",
        goal="Handle and respond to security incidents.",
        backstory="Experienced in incident response and management.",
        allow_delegation=False,
    ),
    "knowledge_update_agent": Agent(
        role="Knowledge Update Specialist",
        goal="Update and manage knowledge base with latest research.",
        backstory="Expert in updating knowledge bases and integrating new findings.",
        allow_delegation=False,
    ),
    "patch_management_agent": Agent(
        role="Patch Management Agent",
        goal="Manage and deploy patches for vulnerabilities.",
        backstory="Specialist in patch management and deployment.",
        allow_delegation=False,
    ),
    "privacy_breach_agent": Agent(
        role="Privacy Breach Agent",
        goal="Handle privacy breaches and related incidents.",
        backstory="Expert in managing privacy breaches and mitigating impacts.",
        allow_delegation=False,
    ),
    "rapid_deployment_agent": Agent(
        role="Rapid Deployment Specialist",
        goal="Deploy and test new strategies and tools quickly.",
        backstory="Specializes in rapid deployment and testing.",
        allow_delegation=False,
    ),
    "report_agent": Agent(
        role="Report Agent",
        goal="Generate and manage comprehensive reports.",
        backstory="Experienced in creating detailed and accurate reports.",
        allow_delegation=False,
    ),
    "research_agent": Agent(
        role="Research Agent",
        goal="Conduct research on emerging vulnerabilities and attack vectors.",
        backstory="Specialist in researching new vulnerabilities and attack techniques.",
        allow_delegation=False,
    ),
    "risk_assessment_agent": Agent(
        role="Risk Assessment Specialist",
        goal="Assess and manage risks associated with smart contracts.",
        backstory="Expert in risk assessment and management.",
        allow_delegation=False,
    ),
    "security_training_agent": Agent(
        role="Security Training Specialist",
        goal="Provide training on security best practices and mitigation strategies.",
        backstory="Specializes in security training and awareness.",
        allow_delegation=False,
    ),
    "social_engineering_agent": Agent(
        role="Social Engineering Specialist",
        goal="Simulate social engineering attacks to test security awareness.",
        backstory="Expert in social engineering techniques and simulations.",
        allow_delegation=False,
    ),
    "threat_intelligence_agent": Agent(
        role="Threat Intelligence Specialist",
        goal="Gather and analyze threat intelligence to inform security strategies.",
        backstory="Specialist in threat intelligence and analysis.",
        allow_delegation=False,
    ),
    "vulnerability_scanner_agent": Agent(
        role="Vulnerability Scanner",
        goal="Run vulnerability scans on smart contracts.",
        backstory="Expert in vulnerability scanning and assessment.",
        allow_delegation=False,
    ),
    "white_hat_agent": Agent(
        role="White Hat Agent",
        goal="Identify and address vulnerabilities from a white hat perspective.",
        backstory="Specializes in ethical hacking and vulnerability identification.",
        allow_delegation=False,
    ),
}

# Define tasks
tasks = [
    Task(
        description="Execute and analyze access control attacks to identify vulnerabilities in permission settings.",
        func=attack_manager,
        expected_output="Detailed report on identified access control issues, including exploitation techniques and recommendations for mitigation.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Simulate and assess adversarial attacks to evaluate the robustness of smart contracts against such threats.",
        func=attack_manager,
        expected_output="A summary of adversarial attack results, including effectiveness and potential impacts.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Identify and exploit vulnerabilities related to business logic in smart contracts.",
        func=attack_manager,
        expected_output="A report detailing business logic flaws and suggested improvements.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for clickjacking vulnerabilities by attempting to deceive users into performing unintended actions.",
        func=attack_manager,
        expected_output="A report on any clickjacking vulnerabilities discovered and suggested countermeasures.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Conduct command injection attacks to check for vulnerabilities that allow unauthorized command execution.",
        func=attack_manager,
        expected_output="Detailed findings on command injection vulnerabilities and recommended fixes.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Evaluate smart contracts for potential vulnerabilities related to consensus mechanisms.",
        func=attack_manager,
        expected_output="Analysis report highlighting consensus vulnerabilities and suggestions for improvements.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Perform cross-site scripting (XSS) attacks to identify vulnerabilities in user input handling.",
        func=attack_manager,
        expected_output="A report detailing XSS vulnerabilities, including exploitation methods and mitigation strategies.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test cryptographic implementations in smart contracts to find weaknesses or flaws.",
        func=attack_manager,
        expected_output="Detailed findings on cryptographic weaknesses and recommendations for securing cryptographic functions.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Develop and test custom exploits based on identified vulnerabilities.",
        func=exploit_generator_agent,
        expected_output="Working custom exploits with documentation on how they exploit the vulnerabilities and their impacts.",
        agent=agents["exploit_generator_agent"]
    ),
    Task(
        description="Identify and exploit data leakage vulnerabilities in smart contracts.",
        func=attack_manager,
        expected_output="A report on data leakage vulnerabilities found, with suggested fixes and impact analysis.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Simulate distributed denial-of-service (DDoS) attacks to test the resilience of smart contracts.",
        func=attack_manager,
        expected_output="Analysis of DDoS attack impact and recommendations for improving resilience.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for vulnerabilities related to `delegatecall` in smart contracts.",
        func=attack_manager,
        expected_output="Findings on delegatecall vulnerabilities with recommendations for securing smart contracts.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Perform denial-of-service attacks to evaluate the contract's handling of such threats.",
        func=attack_manager,
        expected_output="Report on denial-of-service vulnerabilities and suggested improvements.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Conduct denial-of-service attacks to test the smart contract’s resilience against such attacks.",
        func=attack_manager,
        expected_output="Detailed report on the impact of the attacks and recommendations for improvement.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for front-running vulnerabilities in smart contract transactions.",
        func=attack_manager,
        expected_output="A report on front-running issues found and suggestions for mitigating these vulnerabilities.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Simulate integer underflow attacks to identify vulnerabilities in numerical operations.",
        func=attack_manager,
        expected_output="Detailed findings on integer underflow issues and recommendations for code improvements.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Load and utilize adversarial datasets to test the robustness of smart contracts.",
        func=attack_manager,
        expected_output="Analysis of results from testing with adversarial datasets, including any vulnerabilities discovered.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Conduct overflow attacks to identify vulnerabilities related to numerical overflows.",
        func=attack_manager,
        expected_output="Report detailing overflow vulnerabilities and suggested code improvements.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Simulate phishing attacks to identify weaknesses in user interactions and data handling.",
        func=attack_manager,
        expected_output="Findings on phishing vulnerabilities and recommendations for enhancing security.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for race condition vulnerabilities in smart contracts.",
        func=attack_manager,
        expected_output="A report detailing race condition issues and suggestions for mitigation.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Conduct reentrancy attacks to test for vulnerabilities that could be exploited in smart contracts.",
        func=attack_manager,
        expected_output="Detailed findings on reentrancy vulnerabilities and recommendations for securing contracts.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for session fixation vulnerabilities in smart contracts and related systems.",
        func=attack_manager,
        expected_output="A report on session fixation issues and recommendations for improving security.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Identify and address misconfigurations in smart contract deployments.",
        func=attack_manager,
        expected_output="Findings on misconfigurations and suggested corrections to improve security.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for vulnerabilities related to the reconfiguration of smart contracts.",
        func=attack_manager,
        expected_output="Report detailing reconfiguration vulnerabilities and recommendations for secure practices.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Import data into Spirent CyberFlood for further analysis and testing.",
        func=attack_manager,
        expected_output="Successfully imported data with detailed documentation on the import process.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for timestamp dependencies and vulnerabilities in smart contracts.",
        func=attack_manager,
        expected_output="Findings on timestamp-related vulnerabilities and recommendations for improving contract robustness.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Simulate token theft attacks to evaluate the security of token management within smart contracts.",
        func=attack_manager,
        expected_output="A detailed report on token theft vulnerabilities and suggested security enhancements.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for vulnerabilities related to transaction origin in smart contracts.",
        func=attack_manager,
        expected_output="Findings on transaction origin vulnerabilities with recommendations for improving security.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for vulnerabilities related to unchecked low-level calls in smart contracts.",
        func=attack_manager,
        expected_output="A report on vulnerabilities found due to unchecked low-level calls and suggested improvements.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for wallet vulnerabilities and exploits related to smart contracts.",
        func=attack_manager,
        expected_output="Detailed findings on wallet-related vulnerabilities and recommendations for secure practices.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Test for XML external entity (XXE) vulnerabilities in smart contracts and related systems.",
        func=attack_manager,
        expected_output="Report on XXE vulnerabilities with recommendations for enhancing security.",
        agent=agents["attack_manager"]
    ),
    Task(
        description="Perform automated scanning of smart contracts to identify common vulnerabilities.",
        func=audit_agent,
        expected_output="A report on vulnerabilities found through automated scanning with recommendations for remediation.",
        agent=agents["audit_agent"]
    ),
    Task(
        description="Evaluate the code cleanliness of smart contracts to ensure adherence to best practices.",
        func=audit_agent,
        expected_output="Findings on code cleanliness with recommendations for improving code quality.",
        agent=agents["audit_agent"]
    ),
    Task(
        description="Conduct an initial review of smart contract code to identify obvious issues and areas for improvement.",
        func=audit_agent,
        expected_output="Summary of initial findings and suggestions for further detailed analysis.",
        agent=agents["audit_agent"]
    ),
    Task(
        description="Categorize identified issues in smart contracts based on their severity and impact.",
        func=audit_agent,
        expected_output="Categorized list of issues with details on severity and recommended actions.",
        agent=agents["audit_agent"]
    ),
    Task(
        description="Perform a detailed manual review of smart contracts to uncover complex issues not detected by automated tools.",
        func=audit_agent,
        expected_output="Comprehensive manual review report highlighting complex issues and recommendations.",
        agent=agents["audit_agent"]
    ),
    Task(
        description="Continuously monitor and update the security posture of smart contracts.",
        func=audit_agent,
        expected_output="Regular updates on security status and recommendations for ongoing improvements.",
        agent=agents["audit_agent"]
    ),
    Task(
        description="Prepare documentation for the audit process, including methodologies and findings.",
        func=audit_agent,
        expected_output="Well-organized documentation covering the audit process and findings.",
        agent=agents["audit_agent"]
    ),
    Task(
        description="Generate detailed reports based on audit findings, research, and testing results.",
        func=audit_agent,
        expected_output="Comprehensive reports with findings, analysis, and recommendations.",
        agent=agents["audit_agent"]
    ),
    Task(
        description="Update and maintain a knowledge base with recent research, best practices, and vulnerability data.",
        func=knowledge_update_agent,
        expected_output="Knowledge base updated with the latest information, research, and best practices.",
        agent=agents["knowledge_update_agent"]
    ),
    Task(
        description="Review recent research and findings related to smart contract vulnerabilities and exploits.",
        func=knowledge_update_agent,
        expected_output="Summary of recent research with implications for smart contract security.",
        agent=agents["knowledge_update_agent"]
    ),
    Task(
        description="Organize and manage resources related to smart contract security and vulnerability research.",
        func=knowledge_update_agent,
        expected_output="Well-organized resources and research documentation for future reference.",
        agent=agents["knowledge_update_agent"]
    )
]


# Set up manager LLM
manager_llm = ChatOpenAI(model_name="gpt-4")

# Define manager agent
manager = Agent(
    role="Project Manager",
    goal="Oversee the project and ensure high-quality output.",
    backstory="Experienced in managing complex projects and coordinating teams.",
    allow_delegation=True,
    tools=[manager_llm]
)

# Instantiate crew with a custom manager
crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    manager_agent=manager,
    process=Process.hierarchical,
    manager_llm=manager_llm
)

# Start the crew's work
result = crew.kickoff()
logger.info(result)
