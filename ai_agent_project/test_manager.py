from ai_agent_project.manager_agent import manager_agent


document = """
Artificial Intelligence is transforming industries.
AI agents can perform tasks autonomously.
Large Language Models help build intelligent systems.
"""

# Test 1 → Summarization
result1 = manager_agent("summarize", document=document)
print("Summarize Agent Output:")
print(result1)


# Test 2 → Question Answering
result2 = manager_agent("question", document=document, question="What can AI agents do?")
print("\nQuery Agent Output:")
print(result2)


# Test 3 → Internet Search
result3 = manager_agent("search", question="What is Artificial Intelligence?")
print("\nSearch Agent Output:")
print(result3)