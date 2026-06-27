# Emotion Detector Web Application

Final project for the IBM course **Developing AI Applications with Python and Flask**.

This Flask application sends text to the Watson NLP Emotion Predict service and returns scores for anger, disgust, fear, joy, and sadness together with the dominant emotion.

## Project structure

- `EmotionDetection/emotion_detection.py` - Watson NLP client and output formatting
- `EmotionDetection/__init__.py` - package export
- `server.py` - Flask web application
- `test_emotion_detection.py` - unit tests
- `templates/index.html` - user interface
- `static/mywebscript.js` - browser-side request logic

## Run

```bash
pip install -r requirements.txt
python server.py
```

Open `http://localhost:5000`.

## Test and analyze

```bash
python test_emotion_detection.py
pylint server.py EmotionDetection/emotion_detection.py
```
