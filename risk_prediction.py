def predict_disease(skin_type):

    diseases = {

        "oily":[
            "Acne",
            "Blackheads",
            "Whiteheads"
        ],

        "dry":[
            "Eczema",
            "Psoriasis",
            "Skin irritation"
        ],

        "combination":[
            "T-zone acne",
            "Uneven hydration"
        ],

        "normal":[
            "Low risk"
        ]
    }

    return diseases.get(skin_type,[])