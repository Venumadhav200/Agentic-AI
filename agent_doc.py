from transformers import pipeline
import re

# lightweight model (fast)
generator = pipeline("text-generation", model="gpt2")


def summarize_and_extract(document):

    prompt = f"""
Summarize the document in 2 sentences.

Document:
{document}

Summary:
"""

    result = generator(
        prompt,
        max_new_tokens=50,
        num_return_sequences=1
    )

    text = result[0]["generated_text"]

    # remove prompt
    summary = text.replace(prompt, "").strip()

    # keep first 2 sentences
    sentences = re.split(r'[.!?]', summary)
    summary = ". ".join(sentences[:2]).strip() + "."

    # simple keyword extraction
    words = re.findall(r'\b[a-zA-Z]{4,}\b', document.lower())

    keywords = []
    for w in words:
        if w not in keywords:
            keywords.append(w)
        if len(keywords) == 5:
            break

    return {
        "document": summary,
        "keywords": keywords
    }