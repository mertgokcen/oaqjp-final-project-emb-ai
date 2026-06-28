from flask import Flask
from EmotionDetection.emotion_detection import emotion_detector 

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    emotions = emotion_detector(text_to_analyze)
    
    return emotions

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
