from ai_agent_project.agent_doc import summarize_and_extract
from ai_agent_project.agent_search import search_internet
from ai_agent_project.coding_agent import coding_agent


def smart_manager(question, document=None):

    q = question.lower()

    coding_keywords = [
        "python",
        "java",
        "c++",
        "code",
        "program",
        "leetcode",
        "algorithm",
        "debug",
        "sql",
        "binary search",
        "linked list",
        "tree",
        "stack",
        "queue"
    ]

    if document and (
        "summarize" in q
        or "summary" in q
        or "keywords" in q
    ):
        return summarize_and_extract(document)

    if any(word in q for word in coding_keywords):
        return coding_agent(question)

    return search_internet(question)