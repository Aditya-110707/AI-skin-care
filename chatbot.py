def get_chatbot_response(message):

    message=message.lower()

    if "acne" in message:
        return "For acne use salicylic acid cleanser and avoid oily foods."

    elif "dry skin" in message:
        return "Use hydrating moisturizer and hyaluronic acid serum."

    elif "oily skin" in message:
        return "Use oil free moisturizer and salicylic acid cleanser."

    elif "hello" in message or "hi" in message:
        return "Hello! I am your AI dermatologist. Ask me anything about skincare."

    else:
        return "I recommend maintaining a good skincare routine and using sunscreen."