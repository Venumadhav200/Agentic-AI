from agent_doc import summarize_and_extract
from agent_query import answer_query
from agent_search import search_internet


def smart_manager(question, document=None):

    q = question.lower()

    # summarize document
    if document and ("summarize" in q or "summary" in q):
        return summarize_and_extract(document)

    # question from document
    if document:
        return answer_query(document, question)

    # internet search
    return search_internet(question)