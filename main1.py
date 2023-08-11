import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'speechtotext.json'
client = speech.SpeechClient()

audio_file = 'Part.mp3'

with open(audio_file, 'rb') as f:
    content = f.read()
audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    language_code='en-US',
    enable_automatic_punctuation =True,
)

response_standard = client.recognize(
    config=config, 
    audio=audio
    )

print(response_standard.results)