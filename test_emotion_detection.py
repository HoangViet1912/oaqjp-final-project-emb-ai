"""Unit tests for the EmotionDetection package."""

import json
import unittest
from unittest.mock import patch

from EmotionDetection import emotion_detector


class MockResponse:
    """Minimal requests.Response replacement for deterministic unit tests."""

    def __init__(self, status_code, scores=None):
        self.status_code = status_code
        self.text = json.dumps(
            {"emotionPredictions": [{"emotion": scores}]}
        ) if scores is not None else "{}"

    def raise_for_status(self):
        """Raise only when the mocked status represents an HTTP failure."""
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP error: {self.status_code}")


def response_for_text(_url, json=None, **_kwargs):
    """Return Watson-like results for the five required test statements."""
    text = json["raw_document"]["text"]
    dominant_by_text = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear",
    }
    dominant = dominant_by_text[text]
    scores = {
        "anger": 0.03,
        "disgust": 0.02,
        "fear": 0.04,
        "joy": 0.05,
        "sadness": 0.01,
    }
    scores[dominant] = 0.90
    return MockResponse(200, scores)


class TestEmotionDetector(unittest.TestCase):
    """Validate the dominant emotion for all required statements."""

    @patch("EmotionDetection.emotion_detection.requests.post", side_effect=response_for_text)
    def test_joy(self, _mock_post):
        """A glad statement should be classified as joy."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post", side_effect=response_for_text)
    def test_anger(self, _mock_post):
        """A mad statement should be classified as anger."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post", side_effect=response_for_text)
    def test_disgust(self, _mock_post):
        """A disgusted statement should be classified as disgust."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post", side_effect=response_for_text)
    def test_sadness(self, _mock_post):
        """A sad statement should be classified as sadness."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post", side_effect=response_for_text)
    def test_fear(self, _mock_post):
        """An afraid statement should be classified as fear."""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input(self, mock_post):
        """A Watson 400 response should produce the required empty result."""
        mock_post.return_value = MockResponse(400)
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
