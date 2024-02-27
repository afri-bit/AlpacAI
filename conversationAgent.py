
from sdv_llm import get_and_speak_response
from speechToText import speech_to_text


def activate_ecal():
    """_summary_

    Returns:
        _type_: _description_
    """
    # @TODO: integrate eCal listener
    return True

def listen_to_car():
    """_summary_
    """
    activate_ecal()

def play_music():
    """_summary_

    Returns:
        _type_: _description_
    """
    # @TODO: play music
    return True


def generate_conversation():
    """_summary_
    """
    prompt_for_sleepy = "You are a car assistant and the driver is getting sleepy. \
                        What do you say to them? Just one sentence response"

    get_and_speak_response(prompt_for_sleepy)


def warn_driver():
    """_summary_

    Returns:
        _type_: _description_
    """
    # @TODO: Steering vibration, fans
    return True

def detect_drowsiness(drowsiness_level):
    """_summary_

    Args:
        drowsiness_level (_type_): _description_
    """
    if 80 <= drowsiness_level <= 90:
        play_music()
    elif 50 <= drowsiness_level < 80:
        generate_conversation()
    else:
        warn_driver()


if __name__ == "__main__":
    # Invoke speech detection
    # speech_to_text()
    # listen_to_car()
    detect_drowsiness(drowsiness_level=85)
