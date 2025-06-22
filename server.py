''' This server app hosts the API endpoints '''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detection():
    ''' JavaScript calls HTTP GET request to this API when button is clicked '''
    text_to_analyze = request.args.get("textToAnalyze")
    emotions = emotion_detector(text_to_analyze)
    # Handle error
    if not emotions["dominant_emotion"]:
        return "Invalid text! Please try again!"
    # Define text template and variables for response
    res = "For the given statement, the system response is {}. The dominant emotion is {}."
    emotions_only = {key: value for key, value in emotions.items() if key != "dominant_emotion"}
    return res.format(emotions_only, emotions["dominant_emotion"])

@app.route("/")
def home():
    ''' Render index.html as the root directory '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
