from alpacai.core.genai.text_to_speech import TextToSpeech
import ollama


def get_and_speak_response(tts: TextToSpeech, input_text: str):
    """Returns the speech of LLM response given the input text

    Args:
        input_text (str): Text to be input to LLM
    """

    response = ollama.chat(
        model="vicuna",
        messages=[
            {"role": "user", "content": input_text},
        ],
    )
    response_text = response.get("message").get("content")

    print(response_text)

    # Use TTS to speak out the response
    tts.text_to_speech(response_text)
    return response_text


if __name__ == "__main__":
    get_and_speak_response(
        "You are a car assistant and the driver is getting sleepy. \
                        What do you say to them? Just one sentence response"
    )
