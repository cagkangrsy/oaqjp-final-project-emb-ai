"""Flask application for detecting emotions from text."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """Endpoint that analyzes emotions for the provided text."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    parts = [
        f"'{k}': {v}"
        for k, v in response.items()
        if k != "dominant_emotion"
    ]

    joined = ", ".join(parts)
    return (
        f"For the given statement, the system response is {joined}. "
        f"The dominant emotion is {dominant_emotion}."
)

@app.route("/")
def render_index_page():
    """Render the main index page with the input form."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
