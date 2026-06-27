# Submission Guide – Emotion Detector Final Project

## Before submitting

1. Upload this project to a **public GitHub repository**.
2. Run the live commands inside the IBM Skills Network lab so the Watson endpoint is available.
3. Replace the supplied local demo screenshots with screenshots from your own live run when required by the course.

## GitHub commands

```bash
git init
git add .
git commit -m "Complete Emotion Detector final project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/emotion-detector-final-project.git
git push -u origin main
```

## Task 1 – README URL

Submit:

```text
https://github.com/YOUR_USERNAME/emotion-detector-final-project/blob/main/README.md
```

## Task 2 – Watson NLP application

### Activity 1
Paste the contents of:

```text
EmotionDetection/emotion_detection.py
```

### Activity 2
Run in the IBM lab:

```bash
python3.11
```

```python
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector("I love this new technology.")
```

Capture or paste the output showing that import and execution complete without errors.

## Task 3 – Output formatting

### Activity 1
Use the same `emotion_detection.py`. The returned dictionary contains:

```text
anger, disgust, fear, joy, sadness, dominant_emotion
```

### Activity 2
Run:

```python
emotion_detector("I love this new technology.")
```

Confirm that the result is a dictionary with all six keys.

## Task 4 – Package validation

### Activity 1
Submit:

```text
https://github.com/YOUR_USERNAME/emotion-detector-final-project/blob/main/EmotionDetection/__init__.py
```

### Activity 2
Run:

```bash
python3.11
```

```python
from EmotionDetection import emotion_detector
emotion_detector("I hate working long hours.")
```

## Task 5 – Unit tests

### Activity 1
Paste the contents of:

```text
test_emotion_detection.py
```

### Activity 2
Run:

```bash
python3.11 test_emotion_detection.py
```

The included test suite checks joy, anger, disgust, sadness, fear, and the 400-status blank-input case.

## Task 6 – Flask deployment

### Activity 1
Paste the contents of:

```text
server.py
```

### Activity 2
Run:

```bash
python3.11 server.py
```

Open the lab preview, enter:

```text
I think I am having fun
```

Upload a live screenshot named:

```text
6b_deployment_test.png
```

## Task 7 – Error handling

### Activity 1
In `emotion_detection.py`, the `status_code == 400` branch returns `None` for every field.

### Activity 2
In `server.py`, a `None` dominant emotion returns:

```text
Invalid text! Please try again!
```

### Activity 3
Submit a blank input in the live application and upload:

```text
7c_error_handling_interface.png
```

## Task 8 – Static analysis

Run:

```bash
pylint server.py EmotionDetection/emotion_detection.py
```

The supplied code received:

```text
Your code has been rated at 10.00/10
```

## Files included

- `README.md`
- `EmotionDetection/__init__.py`
- `EmotionDetection/emotion_detection.py`
- `server.py`
- `test_emotion_detection.py`
- `templates/index.html`
- `static/mywebscript.js`
- `requirements.txt`
- `6b_deployment_test.png` – local interface demonstration
- `7c_error_handling_interface.png` – local error-interface demonstration
- `test_output.txt`
- `pylint_output.txt`
