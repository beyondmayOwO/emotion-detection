"""Flask server to grab the user input from the client side and return the emotion scores """

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/')
def render_index():
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_text():
    # Get the input that was sent as the query parameter from the client
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    else:
        sadness_score = result['sadness']
        joy_score = result['joy']
        fear_score = result['fear']
        disgust_score = result['disgust']
        anger_score = result['anger']
        dominant_emotion = result['dominant_emotion']
        
        return f"For the given statement, the system response is 'anger': {anger_score}, 'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
