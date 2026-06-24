from ai_agent_project.archive.agent_query import answer_query

document = """
Artificial Intelligence is transforming industries.
AI agents can perform tasks autonomously.
Large Language Models help build intelligent systems.
"""

question = "What can AI agents do?"

result = answer_query(document, question)

print(result)