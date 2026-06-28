"This is docstring."
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector_request():
    "This is docstring."
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    if emotions["dominant_emotion"] is None:
        return "<b> Invalid text! Please try again!</b>"

    result_str = "For the given statement, the system response is "
    for k,v in emotions.items():
        if k != "dominant_emotion":
            result_str += f" \'{k}\':{v},"
    result_str = result_str[:-2]
    dominant_emotion = emotions["dominant_emotion"]
    result_str += f". The dominant emotion is <b>{dominant_emotion}</b>."
    return result_str

@app.route("/")
def render_index_page():
    "This is docstring."
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
