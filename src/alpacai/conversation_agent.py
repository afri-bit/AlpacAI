import random
import time
import googlemaps
import pygame

from alpacai.core.genai.sdv_llm import get_and_speak_response
from alpacai.core.genai.text_to_speech import text_to_speech

GOOGLE_API_KEY = ""


def get_attentiveness_score():
    """Generates dummy attentiveness score

    Returns:
        int: Attentiveness score
    """
    return random.randint(0, 100)

def listen_to_car():
    """Listens to values coming from car
    """
    while True:
        attentiveness_score = get_attentiveness_score()
        print(attentiveness_score)
        check_drowsiness(attentiveness_score)


def play_music(filepath):
    """Play music given the file name

    Returns:
        bool: Returns True if successful
    """
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load MP3 file
    pygame.mixer.music.load(filepath)

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

def play_warning(filepath):
    """Plays warning sound 3 times

    Returns:
        bool: Returns True if successful
    """
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load MP3 file
    pygame.mixer.music.load(filepath)

    # Play the MP3 file
    pygame.mixer.music.play()

    # Since play() is asynchronous, keep the script running until playback is done
    while pygame.mixer.music.get_busy():
        # Check the music playback status every 0.5 seconds
        time.sleep(0.5)
        # input('Press enter to continue...')
        pygame.mixer.music.stop()  # Stop the music
        break  # Exit the loop

    return True


def generate_conversation():
    """Generate conversation with the driver given that they are getting sleepy
    """
    prompt_for_sleepy = "You are a car assistant and the driver is getting sleepy. \
                        What do you say to them? Just one sentence response"

    get_and_speak_response(prompt_for_sleepy)


def warn_driver():
    """Gives the driver haptic and sensual feedback
    """
    # @TODO: Steering vibration, fans
    return True


def check_drowsiness(attentiveness_score):
    """Checks the drowsiness level and takes action according to it

    Args:
        attentiveness_score (int): Level of attentiveness in percentage(0-100)
    """

    if 80 <= attentiveness_score <= 90:
        prompt = "You are a car assistant and the driver is getting sleepy. \
                You want to cheer them up and play some music for them. \
                The music will start after you say your sentence. \
                    Don't write [Music starts playing]"
        # text_to_speech("Let me turn on some music for you.")
        get_and_speak_response(prompt)
        play_music('sounds/electronic-rock-king-around-here-15045.mp3')
    elif 50 <= attentiveness_score < 80:
        flag = random.randint(0,1)
        if flag == 0:
            generate_conversation()
        else:
            make_gps_suggestions(52.5170365, 13.3888599)
    elif attentiveness_score < 50:
        for i in range(3):
            play_warning('sounds/warning.mp3')
        prompt = "You are a car assistant and the driver is getting really really sleepy. \
                You want to warn them firmly with a short message."
        get_and_speak_response(prompt)
        warn_driver()


def make_gps_suggestions(lat, lng):
    """Make suggestions of coffee shops around the driver's GPS location

    Args:
        lat (float): Latitude
        lng (float): Longitude
    """
    gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

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
    
    check_drowsiness(85)
    
    # make_gps_suggestions(52.5170365, 13.3888599)

    # listen_to_car()
