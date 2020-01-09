import requests
import json
from bao_speech import record_audio, read_audio

API_ENDPOINT = 'https://api.wit.ai/speech'
wit_access_token = input("Server access token: ")

def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
    record_audio(num_seconds, AUDIO_FILENAME)
    audio = read_audio(AUDIO_FILENAME)
    headers = {'authorization': 'Bearer ' + wit_access_token, 'Content-Type':
            'audio/wav'}
    resp = requests.post(API_ENDPOINT, headers = headers, data = audio)
    data = json.loads(resp.content)
    text = data['_text']
    return text

if __name__ = '__main__':
    text = RecognizeSpeech('myspeech.wav', 4)
    print("\nYou said: {}".format(text))
