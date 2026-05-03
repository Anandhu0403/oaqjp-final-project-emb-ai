"""
Flask server for Emotion Detection application.
Handles UI rendering and emotion analysis requests.

"""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector


app = Flask(__name__)

@app.route("/")
def home():
    """
    Render the main user interface page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotiondetector():
    """
    Handle emotion detection request from client.
    Accepts text input via query parameter and returns formatted response.
    """
    text = request.args.get("textToAnalyze")

    if not text:
        return "Invalid input! Please try again.",400

    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return  "Invalid text! Please try again!.",400
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
