import cv2
import numpy as np

def extract_skin(image):

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array([0,40,60])
    upper = np.array([20,150,255])

    mask = cv2.inRange(hsv, lower, upper)

    skin = cv2.bitwise_and(image, image, mask=mask)

    return skin


def extract_features(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    mean = np.mean(gray)
    std = np.std(gray)

    # brightness indicator (oil reflection)
    bright_pixels = np.sum(gray > 200)

    return [mean, std, bright_pixels]