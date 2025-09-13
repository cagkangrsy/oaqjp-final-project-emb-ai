# Emotion Detection Web Application

Final project for **IBM Developing AI Applications with Python and Flask** course on Coursera.

A Flask web application that analyzes emotions in text using IBM Watson's NLP service.

## Features

- Web interface for emotion detection
- Detects joy, sadness, anger, fear, and disgust
- Identifies dominant emotion
- RESTful API endpoint

## Setup

1. Install dependencies:
   ```bash
   pip install flask requests
   ```

2. Run the application:
   ```bash
   python server.py
   ```

3. Open `http://localhost:5000` in your browser

## API Usage

**Endpoint**: `/emotionDetector`

**Example**:
```
GET /emotionDetector?textToAnalyze=I am happy today!
```

## Testing

Run unit tests:
```bash
python test_emotion_detection.py
```

## Technologies

- Python, Flask
- IBM Watson NLP API
