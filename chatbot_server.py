from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# ADD YOUR API KEY
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

SYSTEM_PROMPT = """
You are DermaBot, an AI dermatologist assistant for a skincare website.
You help users with:
- skin diseases
- skincare routine
- acne, pigmentation, dryness
- product recommendations
- remedies and prevention

Rules:
1. Answer clearly and simply
2. Give skincare advice
3. Suggest dermatologist visit for serious issues
4. Keep answers short and helpful
"""

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(port=5000, debug=True)