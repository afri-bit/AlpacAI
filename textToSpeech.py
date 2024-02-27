"""Synthesizes speech from the input string of text."""
from google.cloud import texttospeech
from google.oauth2 import service_account
import json

def text_to_speech(txt):

    client = texttospeech.TextToSpeechClient()#(credentials = credentials)

    input_text = texttospeech.SynthesisInput(text=txt)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Studio-O",
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=1
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
   