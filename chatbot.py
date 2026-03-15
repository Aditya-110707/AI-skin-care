import re


def get_chatbot_response(message):

    msg = message.lower()

    intents = {
        "acne": {
            "keywords": ["acne", "pimple", "pimples", "breakout", "zits"],
            "response": (
                "Acne usually occurs due to clogged pores and excess oil. "
                "Use a salicylic acid cleanser, apply niacinamide serum, "
                "avoid touching your face frequently, and maintain a balanced diet."
            ),
        },

        "dry_skin": {
            "keywords": ["dry", "dryness", "flaky", "white patches", "peeling"],
            "response": (
                "Dry skin needs hydration. Use a gentle cleanser, apply a thick moisturizer, "
                "and use hyaluronic acid serum. Also drink at least 2-3 liters of water daily."
            ),
        },

        "oily_skin": {
            "keywords": ["oily", "oil", "greasy", "shiny skin"],
            "response": (
                "Oily skin produces excess sebum. Use salicylic acid facewash, "
                "oil-free moisturizer, and SPF50 sunscreen. Niacinamide serum helps control oil."
            ),
        },

        "dark_spots": {
            "keywords": ["dark spot", "pigmentation", "marks", "uneven skin"],
            "response": (
                "For dark spots use Vitamin C serum, sunscreen daily, and exfoliate weekly. "
                "Turmeric and aloe vera masks may also help naturally."
            ),
        },

        "sunscreen": {
            "keywords": ["sunscreen", "sun protection", "spf"],
            "response": (
                "Use a broad spectrum SPF50 sunscreen. Apply it every morning "
                "and reapply every 3 hours when exposed to sunlight."
            ),
        },

        "routine": {
            "keywords": ["routine", "skincare routine", "daily routine"],
            "response": (
                "Basic skincare routine:\n"
                "Morning: Cleanser → Serum → Moisturizer → Sunscreen\n"
                "Night: Cleanser → Serum → Moisturizer."
            ),
        },

        "diet": {
            "keywords": ["diet", "food", "nutrition", "eat"],
            "response": (
                "For healthy skin: drink 2-3L water daily, eat fruits rich in Vitamin C, "
                "include vegetables and fiber, and reduce oily and processed food."
            ),
        },

        "greeting": {
            "keywords": ["hi", "hello", "hey"],
            "response": (
                "Hello! I'm your AI Dermatologist. Ask me about acne, dry skin, "
                "sunscreen, skincare routine, or diet."
            ),
        },
    }

    # Search for keyword match
    for intent in intents.values():
        for word in intent["keywords"]:
            if re.search(re.escape(word), msg):
                return intent["response"]

    return (
        "I can help with acne, dry skin, oily skin, pigmentation, "
        "sunscreen, skincare routines, and diet tips."
    )