import os
from unicodedata import name
from urllib import response
from google.cloud import texttospeech_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\orine\PycharmProjects\Hackathon23\stt-hackton23-ff184d52e37a.json"
def synthesize_text(text):
    client = texttospeech_v1.TextToSpeechClient()
    input_text = texttospeech_v1.SynthesisInput(text=text)
    voice = texttospeech_v1.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech_v1.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech_v1.AudioConfig(
        audio_encoding=texttospeech_v1.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config
    )

    with open("output.mp3", "wb") as out_file:
        out_file.write(response.audio_content)
        print("Audio content written to file 'output.mp3'")

synthesize_text("Hello, how are you?")
