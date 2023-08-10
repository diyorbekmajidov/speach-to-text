from google.oauth2 import service_account
from google.cloud import speech

client_file = 'speechtotext.json'
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

gcs_uri = 'gcs:<url link>'
config = speech.RecognitionConfig(
    encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz = 44100,
    language_code = 'en-US',
)

audio = speech.RecognitionAudio(uri=gcs_uri)
operation = client.long_running_recognize(config=config, audio=audio)
print('Waiting for operation to complete...')
response = operation.result(timeout=90)
for result in response.results:
    print(result.alternatives[0].transcript)