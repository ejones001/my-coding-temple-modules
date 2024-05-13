# mood_responses.py

def mood_response(mood):
    if mood.lower() == "happy":
        return "Glad to hear that you're happy!"
    elif mood.lower() == "sad":
        return "I'm sorry to hear that you're sad. Is there anything I can do to cheer you up?"
    elif mood.lower() == "excited":
        return "Wow! Sounds like something exciting is happening. Tell me more!"
    else:
        return "Hmm... I'm not sure how to respond to that mood. But I'm here to chat if you'd like!"
