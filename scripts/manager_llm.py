from langchain_openai import ChatOpenAI

# Set up manager LLM
manager_llm = ChatOpenAI(model_name="gpt-4")

# Initialize crew with manager LLM
crew = Crew(
    agents=[research_agent, audit_agent, attack_manager],
    tasks=[research_task, audit_task, attack_task],
    process=Process.hierarchical,
    manager_llm=manager_llm
)
