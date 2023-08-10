import io
from google.oauth2 import service_account
from google.cloud import speech

client_file = 'speechtotext.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

audio_file = 'audio.wav'
with io.open(audio_file, 'rb') as f:
    content = f.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='en-US',
    model = 'video',
)

response = client.recognize(config=config, audio=audio)
print(response.results)