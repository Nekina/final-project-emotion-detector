import requests
import json

def emotion_detector(text_to_analyze):
    # Define parameters for the API POST Request to Watson AI
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    input_obj = { "raw_document": { "text": text_to_analyze } }
    # Execute POST request
    res = requests.post(url, json=input_obj, headers=headers)
    # Handle error
    if (res.status_code == 400):
        return { "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None }
    # Extract only the relevant info as a dictionary
    emotions = json.loads(res.text)["emotionPredictions"][0]["emotion"]
    # Compare values using key=emotions.get then return the key with the highest value
    dominant_emotion = max(emotions, key=emotions.get)
    # Assign new key-value pair to emotions dict
    emotions["dominant_emotion"] = dominant_emotion
    return emotions