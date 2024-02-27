import pyaudio
from google.cloud import speech

# Create a speech client
client = speech.SpeechClient()

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

# Create a stream
def listen_print_loop(responses):
    for response in responses:
        if not response.results:
            continue

        result = response.results[0]
        if not result.alternatives:
            continue

        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))

def main():
    # Microphone stream setup
    audio_interface = pyaudio.PyAudio()
    audio_stream = audio_interface.open(format=pyaudio.paInt16,
                                        channels=1,
                                        rate=RATE,
                                        input=True,
                                        frames_per_buffer=CHUNK)

    # Create the stream request
    stream = (speech.StreamingRecognizeRequest(audio_content=data)
              for data in iter(lambda: audio_stream.read(CHUNK, exception_on_overflow=False), b''))

    # Streaming recognition configuration
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code='en-US')
    streaming_config = speech.StreamingRecognitionConfig(config=config)

    # Start streaming
    responses = client.streaming_recognize(streaming_config, stream)
    
    # Listen to the responses
    listen_print_loop(responses)

if __name__ == '__main__':
    main()
