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

    return response.json()
