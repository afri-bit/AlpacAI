import vertexai
import vertexai.preview.generative_models as generative_models
from google.cloud import aiplatform
from textToSpeech import text_to_speech
from vertexai.preview.generative_models import GenerativeModel


def get_and_speak_response(input_text):
    """Returns the speech of LLM response given the input text

    Args:
        input_text (str): Text to be input to LLM
    """
    aiplatform.init(project="bosch-bcx-hack24ber-2308")
    vertexai.init()
    config = {
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    }
    # Initialize your model (if needed, adjust according to your actual setup)
    model = GenerativeModel("gemini-1.0-pro-001")

    chat = model.start_chat()
    # Get the response from the model based on the input text
    response = chat.send_message(input_text, generation_config=config, safety_settings={
        generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    })

    response_text = response.candidates[0].content.parts[0].text

    print(response_text)

    # Use TTS to speak out the response
    text_to_speech(response_text)
    return response_text
