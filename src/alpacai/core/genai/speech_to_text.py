from google.cloud import speech
from alpacai.core.genai.sdv_llm import get_and_speak_response
import deepspeech
import numpy as np
import wave

# Create a speech client
client = speech.SpeechClient()

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms


def listen_print_loop(responses):
    """Listens to microphone until the keyword is being heard

    Args:
        responses (StreamingRecognizeResponse): Response from stream recognizer
        keyword (str): The keyword to trigger LLM
    """
    for response in responses:
        if not response.results:
            continue

        result = response.results[0]
        if not result.alternatives:
            continue

        # The first alternative is the most likely one for this portion.
        print("Transcript: {}".format(result.alternatives[0].transcript))
        transcript = result.alternatives[0].transcript
        # Check if the keyword 'alpaca' is in the transcript
        if "alpaca" in transcript.lower() or "alpaka" in transcript.lower():
            print("Keyword 'alpaca' detected!")
            print(transcript)
            transcript = transcript.replace("alpaka", "")
            transcript = transcript.replace("alpaca", "")
            get_and_speak_response(transcript)
            # continuous_chat_with_voice(transcript)


# def speech_to_text():
#     """Listens the microphone continuously
#     """
#     # Microphone stream setup
#     audio_interface = pyaudio.PyAudio()
#     audio_stream = audio_interface.open(format=pyaudio.paInt16,
#                                         channels=1,
#                                         rate=RATE,
#                                         input=True,
#                                         frames_per_buffer=CHUNK)

#     # Create the stream request
#     stream = (speech.StreamingRecognizeRequest(audio_content=data)
#               for data in iter(lambda: audio_stream.read(CHUNK, exception_on_overflow=False), b''))

#     # Streaming recognition configuration
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=RATE,
#         language_code='en-US')
#     streaming_config = speech.StreamingRecognitionConfig(config=config)

#     # Start streaming
#     responses = client.streaming_recognize(streaming_config, stream)

#     # Listen to the responses
#     listen_print_loop(responses)


def speech_to_text(audio_file_path, model_path="deepspeech-0.9.3-models.pbmm"):
    """
    Converts speech to text using Mozilla's STT.

    Parameters:
    - audio_file_path: Path to the audio file to convert.
    - model_path: Path to the DeepSpeech model file.

    Returns:
    The transcribed text.
    """
    # Load the model
    model = deepspeech.Model(model_path)

    # Read the audio file
    with wave.open(audio_file_path, "rb") as audio_file:
        audio_data = np.frombuffer(
            audio_file.readframes(audio_file.getnframes()), np.int16
        )

    # Perform STT
    text = model.stt(audio_data)
    return text


if __name__ == "__main__":
    speech_to_text()
