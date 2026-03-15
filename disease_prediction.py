def predict_disease(skin_type):

    diseases = {

        "dry":[
            "eczema",
            "psoriasis",
            "skin irritation"
        ],

        "oily":[
            "acne",
            "blackheads",
            "large pores"
        ],

        "normal":[
            "low risk"
        ],

        "combination":[
            "t-zone acne",
            "uneven hydration"
        ]
    }

    return diseases.get(skin_type,["unknown"])