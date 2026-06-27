"""Detect emotions in text using the Watson NLP Emotion Predict service."""

import json

import requests

EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}
EMPTY_RESULT = {
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None,
}


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion for the supplied text."""
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(
        EMOTION_URL,
        json=input_json,
        headers=HEADERS,
        timeout=30,
    )

    if response.status_code == 400:
        return EMPTY_RESULT.copy()

    response.raise_for_status()
    formatted_response = json.loads(response.text)
    emotion_data = formatted_response["emotionPredictions"][0]["emotion"]

    scores = {
        "anger": emotion_data["anger"],
        "disgust": emotion_data["disgust"],
        "fear": emotion_data["fear"],
        "joy": emotion_data["joy"],
        "sadness": emotion_data["sadness"],
    }
    dominant_emotion = max(scores, key=scores.get)

    return {**scores, "dominant_emotion": dominant_emotion}
