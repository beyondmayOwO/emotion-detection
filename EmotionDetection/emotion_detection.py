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

    # Change format from json to dictionary
    dict_response = response.json()

    emotion_scores = {
        'sadness': None,
        'joy': None,
        'fear': None,
        'disgust': None,
        'anger': None,
    }

    if response.status_code == 200:
        emotions = dict_response['keywords'][0]['emotion']

        # Get method for dictionary to extract each key (score) from emotions and assign to the respective emotion scores
        for emotion in emotion_scores:
            emotion_scores[emotion] = emotions.get(emotion, 0)

        # Max function for dictionary to find the dominant emotion, the emotion with the highest score
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Add dominant_emotion to emotion_scores
        emotion_scores['dominant_emotion'] = dominant_emotion
        
        return emotion_scores
    elif response.status_code == 400:
        emotion_scores['dominant_emotion'] = None

        return emotion_scores
