
import random
import time

# from speechToText import speech_to_text
import googlemaps
import pygame

from sdv_llm import get_and_speak_response
from textToSpeech import text_to_speech


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
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load your MP3 file
    pygame.mixer.music.load('electronic-rock-king-around-here-15045.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Since play() is asynchronous, keep the script running until playback is done
    while pygame.mixer.music.get_busy():
        # Check the music playback status every 0.1 seconds
        time.sleep(0.1)
        input('Press enter to continue...')
        pygame.mixer.music.stop()  # Stop the music
        break  # Exit the loop

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
        text_to_speech("Let me turn on some music for you.")
        play_music()
    elif 50 <= drowsiness_level < 80:
        generate_conversation()
    else:
        warn_driver()

def make_gps_suggestions(lat,lng):
    """_summary_

    Args:
        lat (_type_): _description_
        lng (_type_): _description_
    """
    gmaps = googlemaps.Client(key='GOOGLE_API_KEY')

    # Making a request to the Places API to find restaurants within 500 meters
    places_result = gmaps.places_nearby(location=(lat, lng), radius=500, type='cafe')

    # Parsing and printing the names of places found
    for place in places_result['results']:
        print(place['name'])

    place = random.choice(places_result['results'])
    get_and_speak_response(f"You are a car assistant and the driver is getting sleepy. \
                            And you will recommend them a coffee shop. \
                           The name of the coffee shop is {place}")


if __name__ == "__main__":
    # Invoke speech detection
    # speech_to_text()
    # listen_to_car()

    # detect_drowsiness(drowsiness_level=65)

    make_gps_suggestions(52.5170365, 13.3888599)
