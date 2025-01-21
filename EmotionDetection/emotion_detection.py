"""Extract the different emotion scores and the dominant emotion of the text using Watson NLU API"""

import os
import requests
from dotenv import load_dotenv

load_dotenv('ibm-credentials.env')

API_KEY = os.getenv("NATURAL_LANGUAGE_UNDERSTANDING_APIKEY")
API_URL = os.getenv("NATURAL_LANGUAGE_UNDERSTANDING_URL")
API_VERSION = "/v1/analyze?version=2019-07-12"

def emotion_detector(text_to_analyze):
    url = f"{API_URL}{API_VERSION}"
    header = {"Content-Type": "application/json"}
    myobj = {
        "text": text_to_analyze,
        "features": { 
            "keywords": {
                "emotion": True
            }
        }
    }
    response = requests.post(url, headers=header, json=myobj, auth=('apikey', API_KEY), timeout=10) 

    # Extract emotion scores
    dict_response = response.json()
    sadness_score = dict_response['keywords'][0]['emotion']['sadness']
    joy_score = dict_response['keywords'][0]['emotion']['joy']
    fear_score = dict_response['keywords'][0]['emotion']['fear']
    disgust_score = dict_response['keywords'][0]['emotion']['disgust']
    anger_score = dict_response['keywords'][0]['emotion']['anger']

    emotion_scores = {
        'sadness': sadness_score,
        'joy': joy_score,
        'fear': fear_score,
        'disgust': disgust_score,
        'anger': anger_score
    }

    # Max function for dictionary to find the dominant emotion, the emotion with the highest score
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Add the dominant emotion to the dictionary
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
