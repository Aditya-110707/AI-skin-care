import cv2
import pickle
from skin_features import extract_skin, extract_features
from disease_prediction import predict_disease

# LOAD TRAINED MODEL
model = pickle.load(open("model/skin_model.pkl", "rb"))

# FACE DETECTOR
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# OPEN CAMERA
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# SET CAMERA RESOLUTION (prevents blank frames)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# CHECK CAMERA
if not cap.isOpened():
    print("Camera not detected")
    exit()

while True:

    ret, frame = cap.read()

    # CHECK FRAME
    if not ret or frame is None:
        print("Failed to grab frame")
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        face = frame[y:y+h, x:x+w]

        # Extract skin region
        skin = extract_skin(face)

        # Extract features
        features = extract_features(skin)

        # Predict skin type
        prediction = model.predict([features])[0]

        # Predict possible diseases
        diseases = predict_disease(prediction)

        disease_text = ", ".join(diseases)

        # DRAW FACE BOX
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        # SHOW SKIN TYPE
        cv2.putText(
            frame,
            "Skin: " + str(prediction),
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

        # SHOW RISK
        cv2.putText(
            frame,
            "Risk: " + disease_text,
            (x, y+h+25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255,255,255),
            2
        )

    cv2.imshow("SkinSense Scanner", frame)

    # PRESS Q TO EXIT
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()