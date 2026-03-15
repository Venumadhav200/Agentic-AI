chat_memory = []

def add_message(role, content):
    chat_memory.append({"role": role, "content": content})

def get_memory():
    return chat_memory[-10:]