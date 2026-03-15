import cv2
import numpy as np
import pickle
import random
from flask import Flask, render_template, request, jsonify

from skin_features import extract_skin, extract_features
from disease_prediction import predict_disease
from chatbot import get_chatbot_response

app = Flask(__name__)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = pickle.load(open("model/skin_model.pkl", "rb"))

# FACE DETECTOR
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# -----------------------------
# SKINCARE DATABASE
# -----------------------------
skin_data = {

    "oily": {
        "recommendation": [
            "Use oil-free SPF 50 sunscreen",
            "Use salicylic acid facewash",
            "Apply gel-based moisturizer"
        ],
        "serums": [
            "Niacinamide serum",
            "Salicylic acid serum",
            "Tea tree serum"
        ],
        "herbal": [
            "Multani mitti mask twice a week",
            "Turmeric + yogurt mask",
            "Aloe vera gel overnight"
        ],
        "products": [
            {"name": "Mamaearth Tea Tree Face Wash", "link": "https://mamaearth.in/product/tea-tree-face-wash"},
            {"name": "Mamaearth Oil Free Moisturizer", "link": "https://mamaearth.in/product/oil-free-face-moisturizer"},
            {"name": "Mamaearth Ultra Light Sunscreen SPF50", "link": "https://mamaearth.in/product/ultra-light-sunscreen"},
            {"name": "Mamaearth Niacinamide Serum", "link": "https://mamaearth.in/product/niacinamide-serum"}
        ],
        "routine": [
            "Morning: Facewash → Niacinamide → Moisturizer → SPF",
            "Afternoon: Wash face with water",
            "Night: Facewash → Salicylic Serum → Aloe vera gel"
        ],
        "diet": [
            "Drink minimum 2.5L water",
            "Eat fruits rich in Vitamin C",
            "Reduce oily foods"
        ]
    },

    "dry": {
        "recommendation": [
            "Use hydrating facewash",
            "Apply thick moisturizer",
            "Use SPF 50 sunscreen daily"
        ],
        "serums": [
            "Hyaluronic acid serum",
            "Vitamin E serum",
            "Ceramide serum"
        ],
        "herbal": [
            "Honey + milk mask",
            "Banana + honey mask",
            "Aloe vera hydration mask"
        ],
        "products": [
            {"name": "Mamaearth Rice Face Wash", "link": "https://mamaearth.in/product/rice-face-wash"},
            {"name": "Mamaearth Moisturizing Cream", "link": "https://mamaearth.in/product/moisturizing-cream"},
            {"name": "Mamaearth Hydrating Sunscreen", "link": "https://mamaearth.in/product/hydrating-sunscreen"},
            {"name": "Mamaearth Hyaluronic Acid Serum", "link": "https://mamaearth.in/product/hyaluronic-acid-serum"}
        ],
        "routine": [
            "Morning: Cleanser → Hyaluronic Serum → Moisturizer → SPF",
            "Evening: Hydrating serum",
            "Night: Moisturizer overnight"
        ],
        "diet": [
            "Drink 2L water daily",
            "Eat nuts and seeds",
            "Increase healthy fats"
        ]
    },

    "normal": {
        "recommendation": [
            "Use mild facewash",
            "Apply SPF 50 sunscreen",
            "Maintain balanced skincare"
        ],
        "serums": [
            "Vitamin C serum",
            "Niacinamide serum",
            "Hyaluronic acid serum"
        ],
        "herbal": [
            "Coffee scrub weekly",
            "Turmeric + honey mask",
            "Cucumber cooling mask"
        ],
        "products": [
            {"name": "Mamaearth Vitamin C Face Wash", "link": "https://mamaearth.in/product/vitamin-c-face-wash"},
            {"name": "Mamaearth Vitamin C Moisturizer", "link": "https://mamaearth.in/product/vitamin-c-moisturizer"},
            {"name": "Mamaearth Vitamin C Sunscreen", "link": "https://mamaearth.in/product/vitamin-c-sunscreen"},
            {"name": "Mamaearth Vitamin C Serum", "link": "https://mamaearth.in/product/vitamin-c-serum"}
        ],
        "routine": [
            "Morning: Cleanser → Vitamin C Serum → Moisturizer → SPF",
            "Night: Cleanser → Niacinamide Serum → Moisturizer"
        ],
        "diet": [
            "Drink 2L water daily",
            "Eat fruits daily",
            "Increase vegetables"
        ]
    },

    "combination": {
        "recommendation": [
            "Use gentle foaming cleanser",
            "Apply lightweight moisturizer",
            "Use SPF sunscreen daily"
        ],
        "serums": [
            "Niacinamide serum",
            "Hyaluronic acid serum",
            "Vitamin C serum"
        ],
        "herbal": [
            "Aloe vera mask",
            "Cucumber mask",
            "Honey + yogurt mask"
        ],
        "products": [
            {"name": "Mamaearth Ubtan Face Wash", "link": "https://mamaearth.in/product/ubtan-face-wash"},
            {"name": "Mamaearth Oil Free Moisturizer", "link": "https://mamaearth.in/product/oil-free-face-moisturizer"},
            {"name": "Mamaearth Niacinamide Serum", "link": "https://mamaearth.in/product/niacinamide-serum"}
        ],
        "routine": [
            "Morning: Cleanser → Niacinamide Serum → Moisturizer → SPF",
            "Night: Cleanser → Hydration Serum → Moisturizer"
        ],
        "diet": [
            "Drink 2L water daily",
            "Eat fruits and fiber",
            "Limit sugary foods"
        ]
    }
}

# -----------------------------
# HOME PAGE
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# AI ANALYSIS
# -----------------------------
@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["image"]

    img = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(img, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=4,
        minSize=(80, 80)
    )

    if len(faces) == 0:
        return jsonify({"error": "Face not detected"})

    x, y, w, h = faces[0]
    face = frame[y:y+h, x:x+w]

    skin = extract_skin(face)
    features = extract_features(skin)

    prediction = model.predict([features])[0]
    skin_type = str(prediction)

    diseases = predict_disease(prediction)

    skin_score = random.randint(70, 95)

    if skin_type not in skin_data:
        skin_type = "normal"

    info = skin_data[skin_type]

    return jsonify({
        "skin_type": skin_type,
        "skin_score": skin_score,
        "diseases": diseases,
        "recommendation": info["recommendation"],
        "serums": info["serums"],
        "herbal": info["herbal"],
        "products": info["products"],
        "routine": info["routine"],
        "diet": info["diet"]
    })

# -----------------------------
# CHATBOT
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():

    data=request.get_json()

    message=data["message"]

    reply=get_chatbot_response(message)

    return jsonify({"reply":reply})



import requests
from flask import request, jsonify

@app.route("/dermatologists")
def dermatologists():

    lat = request.args.get("lat")
    lon = request.args.get("lon")

    query = f"""
    [out:json];
    (
      node["amenity"="clinic"](around:8000,{lat},{lon});
      node["amenity"="hospital"](around:8000,{lat},{lon});
      node["healthcare"="doctor"](around:8000,{lat},{lon});
    );
    out;
    """

    url = "https://overpass-api.de/api/interpreter"

    response = requests.post(url, data=query)
    data = response.json()

    keywords = ["skin", "derma", "dermatology"]

    doctors = []

    for place in data["elements"]:

        name = place["tags"].get("name","").lower()

        if any(k in name for k in keywords):

            doctors.append({
                "name": place["tags"].get("name"),
                "address": place["tags"].get("addr:full","Nearby clinic"),
                "rating": 4,
                "lat": place["lat"],
                "lon": place["lon"]
            })

    # fallback if no dermatology name found
    if len(doctors) == 0:

        for place in data["elements"][:5]:

            doctors.append({
                "name": place["tags"].get("name","Clinic"),
                "address": "Nearby clinic",
                "rating": 4,
                "lat": place["lat"],
                "lon": place["lon"]
            })

    return jsonify(doctors[:5])

# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)