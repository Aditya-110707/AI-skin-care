import random

def generate_skin_score():
    return random.randint(65, 95)


def get_recommendations(skin_type):

    data = {

        "oily": {
            "recommendation": [
                "Use oil-free SPF 50 sunscreen",
                "Use salicylic acid facewash twice daily",
                "Apply lightweight gel moisturizer"
            ],
            "herbal": [
                "Multani mitti mask twice a week",
                "Turmeric + yogurt mask",
                "Aloe vera gel overnight"
            ],
            "products": [
                {
                    "name": "Mamaearth Tea Tree Face Wash",
                    "link": "https://mamaearth.in/product/tea-tree-face-wash"
                },
                {
                    "name": "Mamaearth Oil Free Face Moisturizer",
                    "link": "https://mamaearth.in/product/oil-free-face-moisturizer"
                },
                {
                    "name": "Mamaearth Ultra Light Sunscreen SPF50",
                    "link": "https://mamaearth.in/product/ultra-light-sunscreen"
                }
            ],
            "routine": [
                "Morning: Cleanser → Moisturizer → SPF 50",
                "Afternoon: Wash face with water",
                "Night: Facewash → Aloe vera gel"
            ],
            "diet": [
                "Drink minimum 2.5L water daily",
                "Reduce oily food",
                "Increase fruits rich in Vitamin C"
            ]
        },

        "dry": {
            "recommendation": [
                "Use cream-based moisturizer",
                "Use hydrating cleanser",
                "Apply SPF 50 sunscreen daily"
            ],
            "herbal": [
                "Honey + milk face mask",
                "Aloe vera gel hydration mask",
                "Banana + honey nourishing mask"
            ],
            "products": [
                {
                    "name": "Mamaearth Rice Face Wash",
                    "link": "https://mamaearth.in/product/rice-face-wash"
                },
                {
                    "name": "Mamaearth Moisturizing Cream",
                    "link": "https://mamaearth.in/product/moisturizing-cream"
                },
                {
                    "name": "Mamaearth Hydrating Sunscreen SPF50",
                    "link": "https://mamaearth.in/product/hydrating-sunscreen"
                }
            ],
            "routine": [
                "Morning: Gentle cleanser → Moisturizer → Sunscreen",
                "Evening: Wash face → Apply hydrating serum",
                "Night: Moisturizer overnight"
            ],
            "diet": [
                "Drink 2L water minimum",
                "Add nuts and seeds",
                "Increase healthy fats like avocado"
            ]
        },

        "normal": {
            "recommendation": [
                "Maintain balanced skincare",
                "Use SPF 50 sunscreen daily",
                "Use mild face cleanser"
            ],
            "herbal": [
                "Coffee scrub once a week",
                "Turmeric + honey glow mask",
                "Cucumber cooling mask"
            ],
            "products": [
                {
                    "name": "Mamaearth Vitamin C Face Wash",
                    "link": "https://mamaearth.in/product/vitamin-c-face-wash"
                },
                {
                    "name": "Mamaearth Vitamin C Moisturizer",
                    "link": "https://mamaearth.in/product/vitamin-c-moisturizer"
                },
                {
                    "name": "Mamaearth Vitamin C Sunscreen SPF50",
                    "link": "https://mamaearth.in/product/vitamin-c-sunscreen"
                }
            ],
            "routine": [
                "Morning: Cleanser → Moisturizer → SPF",
                "Night: Cleanser → Moisturizer"
            ],
            "diet": [
                "Drink 2L water",
                "Add green vegetables",
                "Eat fruits daily"
            ]
        }
    }

    if skin_type not in data:
        skin_type = "normal"

    result = data[skin_type]

    return {
        "skin_score": generate_skin_score(),
        "recommendation": result["recommendation"],
        "herbal": result["herbal"],
        "products": result["products"],
        "routine": result["routine"],
        "diet": result["diet"]
    }