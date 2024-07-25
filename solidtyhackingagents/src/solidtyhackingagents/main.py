import sys
import os
import yaml
from pathlib import Path
from langchain_community.llms import Ollama
import os
os.environ["OPENAI_API_KEY"] = "NA"

llm = Ollama(
    model = "llama3",
    base_url = "http://localhost:11434")
# Add the project root to the Python path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from crewai import Agent, Task, Crew, Process
from solidtyhackingagents.tools.hacktool import setup_logger
from solidtyhackingagents.tools.hacktool import analyze_results
from solidtyhackingagents.tools.hacktool import (
    assign_task, attack_manager, audit_agent, basic_error_agent,
    behavioral_analysis_agent, black_hat_agent, compliance_check_agent,
    configure_crew, define_agent, disaster_recovery_agent,
    economic_attack_agent, exploit_generator_agent, forensics_agent,
    incident_response_agent, knowledge_update_agent, patch_management_agent,
    privacy_breach_agent, rapid_deployment_agent, report_agent,
    research_agent, risk_assessment_agent, security_training_agent,
    social_engineering_agent, threat_intelligence_agent,
    vulnerability_scanner_agent, white_hat_agent
)
from solidtyhackingagents.tools.hacktool import (
    access_control_attack, adversarial_attacks, business_logic_attack,
    clickjacking_attack, command_injection_attack, consensus_attack,
    cross_site_scripting_attack, cryptographic_attack, custom_exploit,
    data_leakage_attack, ddos_attack, delegatecall_attack,
    denial_of_service_attack, dos_attack, front_running_attack,
    integer_underflow_attack, load_adversarial_datasets, overflow_attack,
    phishing_attack, race_condition_attack, reentrancy_attack,
    session_fixation_attack, smart_contract_misconfiguration,
    smart_contract_reconfiguration_attack, timestamp_dependency_attack,
    token_theft_attack, tx_origin_attack, unchecked_low_level_calls,
    wallet_exploit
)

# Import auditing tools
from solidtyhackingagents.tools.hacktool import (
    automated_scanning, code_cleanliness, initial_review,
    issue_categorization, manual_review, ongoing_security,
    preparation_documentation, report_generation,
    retesting_verification, testing
)



from solidtyhackingagents.tools.hacktool import (
    formal_verification, fuzz_testing, invariant_testing,
    performance_testing, scalability_testing, security_audit_tools,
    upgradeable_contracts
)

# Setup logging
logger = setup_logger(name='solidtyhackingagents', log_file='solidtyhackingagents.log')

def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Load configurations
agents_config = load_config(project_root / 'src' / 'solidtyhackingagents' / 'config' / 'agents.yaml')
tasks_config = load_config(project_root / 'src' / 'solidtyhackingagents' / 'config' / 'tasks.yaml')



# Create agents
agents = {}
for agent_name, agent_config in agents_config.items():
    agents[agent_name] = Agent(
        role=agent_config['role'],
        goal=agent_config['goal'],
        backstory=agent_config['backstory'],
        allow_delegation=agent_config.get('allow_delegation', False),
        llm= llm
    )

# Create tasks
tasks = []
for task_config in tasks_config:
    task_function = globals().get(task_config['function'])
    if task_function:
        tasks.append(Task(
            description=task_config['description'],
            func=task_function,
            expected_output=task_config['expected_output'],
            agent=agents[task_config['agent']]
        ))

# Define manager agent using LLaMA 3
manager = Agent(
    role="Project Manager",
    goal="Oversee the project and ensure high-quality output.",
    backstory="Experienced in managing complex projects and coordinating teams.",
    allow_delegation=True,
    llm= llm
)

# Instantiate crew
crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,
    manager_agent=manager,
    process=Process.hierarchical
)

def main():
    logger.info("Starting SolidityHackingAgents analysis with LLaMA 3")
    
    try:
        # Start the crew's work
        result = crew.kickoff()
        logger.info(f"Crew analysis completed. Raw result: {result}")
        
        # Analyze results
        analyzed_results = analyze_results(result)
        logger.info(f"Results analyzed: {analyzed_results}")
        
        # Generate final report
        #final_report = generate_final_report(analyzed_results)
        logger.info("Final report generated")
        
        # Save final report
       # with open('final_security_report.json', 'w') as f:
           # json.dump(final_report, f, indent=4)
        logger.info("Final report saved to final_security_report.json")
        
       
        
        # Run continuous learning pipeline
        from solidtyhackingagents.tools.hacktool import run_pipeline
        run_pipeline(analyzed_results)
        logger.info("Continuous learning pipeline executed")
        
        
        
        # Run testing procedures
        formal_verification.verify()
        fuzz_testing.run()
        invariant_testing.test()
        performance_testing.evaluate()
        scalability_testing.test()
        security_audit_tools.audit()
        upgradeable_contracts.check()
        logger.info("Testing completed")

        # Run all defined agent functions
        assign_task()
        attack_manager()
        audit_agent()
        basic_error_agent()
        behavioral_analysis_agent()
        black_hat_agent()
        compliance_check_agent()
        configure_crew()
        define_agent()
        disaster_recovery_agent()
        economic_attack_agent()
        exploit_generator_agent()
        forensics_agent()
        incident_response_agent()
        knowledge_update_agent()
        patch_management_agent()
        privacy_breach_agent()
        rapid_deployment_agent()
        report_agent()
        research_agent()
        risk_assessment_agent()
        security_training_agent()
        social_engineering_agent()
        threat_intelligence_agent()
        vulnerability_scanner_agent()
        white_hat_agent()
        
        # Run all defined attack methods
        access_control_attack()
        adversarial_attacks()
        business_logic_attack()
        clickjacking_attack()
        command_injection_attack()
        consensus_attack()
        cross_site_scripting_attack()
        cryptographic_attack()
        custom_exploit()
        data_leakage_attack()
        ddos_attack()
        delegatecall_attack()
        denial_of_service_attack()
        dos_attack()
        front_running_attack()
        integer_underflow_attack()
        load_adversarial_datasets()
        overflow_attack()
        phishing_attack()
        race_condition_attack()
        reentrancy_attack()
        session_fixation_attack()
        smart_contract_misconfiguration()
        smart_contract_reconfiguration_attack()
        timestamp_dependency_attack()
        token_theft_attack()
        tx_origin_attack()
        unchecked_low_level_calls()
        wallet_exploit()
    
      
        # Audit-related functions
        automated_scanning()
        # Audit-related functions
        automated_scanning()
        code_cleanliness()
        initial_review()
        issue_categorization()
        manual_review()
        ongoing_security()
        preparation_documentation()
        report_generation()
        retesting_verification()
        testing()



    except Exception as e:
        logger.error(f"An error occurred during the analysis: {str(e)}", exc_info=True)
    
    logger.info("SolidityHackingAgents analysis with LLaMA 3 completed")

if __name__ == "__main__":
    main()
