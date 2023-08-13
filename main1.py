import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'speechtotext.json'
client = speech.SpeechClient()

audio_file = 'Part.mp3'
audio_wav = 'Part.wav'

with open(audio_file, 'rb') as f1:
    content = f1.read()
audio = speech.RecognitionAudio(content=content)

with open(audio_wav, 'rb') as f2:
    content_wav = f2.read()
audio_wav = speech.RecognitionAudio(content=content_wav)

config = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    language_code='en-US',
    enable_automatic_punctuation =True,
)

config_wav = speech.RecognitionConfig(
    sample_rate_hertz=44100,
    language_code='en-US',
    enable_automatic_punctuation =True,
    audio_channel_count = 2, 
    encoding = speech.RecognitionConfig.AudioEncoding.LINEAR16,
)

response_standard = client.recognize(
    config=config, 
    audio=audio
    )

response_wav = client.recognize(
    config=config_wav,
    audio=audio_wav
    )

# print(response_wav.results)
print(response_standard.results[0].alternatives[0].transcript)

# katta file lar uchun

# media_url = 'gs://speech_buckets-1/audio-files/audio.wav'
# lon_audio = speech.RecognitionAudio(uri=media_url)

# config_wav = speech.RecognitionConfig(
#     sample_rate_hertz=48000,
#     language_code='en-US',
#     enable_automatic_punctuation =True,
#     model = 'video',
#     use_enhanced = True,
# )

# operation = client.long_running_recognize(
#     config=config_wav,
#     audio=lon_audio
#     )

# print(operation.result(timeout=90))