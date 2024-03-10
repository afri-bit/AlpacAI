import argparse
import random
import sys
import time
import json

import googlemaps
import pygame
from kuksa_client.grpc import VSSClient

from alpacai.core.genai.sdv_llm import get_and_speak_response
from alpacai.core.genai.text_to_speech import TextToSpeech

GOOGLE_API_KEY = ""

API_DISTRACTION_LEVEL = "Vehicle.Driver.DistractionLevel"
API_FATIGUE_LEVEL = "Vehicle.Driver.FatigueLevel"
API_VEHICLE_SPEED = "Vehicle.Speed"

global client

global sequence
global sequence_number
global simulation


def get_attentiveness_score() -> int:
    """Generates dummy attentiveness score

    Returns:
        int: Attentiveness score
    """
    global simulation
    global sequence
    global sequence_number
    global client

    if simulation:
        if sequence_number < len(sequence):
            sequence_number = sequence_number + 1
            return sequence[sequence_number]
        else:
            return 100  # Always return after 100 after sequence ends
    else:  # Real data
        currect_attentive_probability_values = client.get_current_values(
            ["Vehicle.Driver.AttentiveProbability"]
        )

        current_value = currect_attentive_probability_values[
            "Vehicle.Driver.AttentiveProbability"
        ].value

    return current_value


def listen_to_car(tts):
    """Listens to values coming from car"""
    while True:
        attentiveness_score = get_attentiveness_score()
        print(attentiveness_score)
        check_drowsiness(tts, attentiveness_score)


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
        input("Press enter to continue...")
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


def generate_conversation(tts):
    """Generate conversation with the driver given that they are getting sleepy"""
    prompt_for_sleepy = "You are a car assistant and the driver is getting sleepy. \
                        What do you say to them? Just one sentence response"

    get_and_speak_response(tts, prompt_for_sleepy)


def warn_driver():
    """Gives the driver haptic and sensual feedback"""
    # @TODO: Steering vibration, fans
    return True


def check_drowsiness(tts, attentiveness_score):
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
        get_and_speak_response(tts, prompt)
        play_music("sounds/electronic-rock-king-around-here-15045.mp3")
    elif 50 <= attentiveness_score < 80:
        flag = random.randint(0, 1)
        if flag == 0:
            generate_conversation(tts)
        else:
            make_gps_suggestions(tts, 52.5170365, 13.3888599)
    elif attentiveness_score < 50:
        for i in range(3):
            play_warning("sounds/warning.mp3")
        prompt = "You are a car assistant and the driver is getting really really sleepy. \
                You want to warn them firmly with a short message."
        get_and_speak_response(tts, prompt)
        warn_driver()


def make_gps_suggestions(tts, lat, lng):
    """Make suggestions of coffee shops around the driver's GPS location

    Args:
        lat (float): Latitude
        lng (float): Longitude
    """
    gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

    # Making a request to the Places API to find restaurants within 500 meters
    places_result = gmaps.places_nearby(location=(lat, lng), radius=500, type="cafe")

    # Parsing and printing the names of places found
    for place in places_result["results"]:
        print(place["name"])

    place = random.choice(places_result["results"])
    get_and_speak_response(
        tts,
        f"You are a car assistant and the driver is getting sleepy. \
                            And you will recommend them a coffee shop. \
                           The name of the coffee shop is {place}",
    )


def run():
    tts = TextToSpeech()
    parser = argparse.ArgumentParser(
        prog="AttentiveAI",
        description="Intelligent driver drowsiness avoidance with GenAI",
    )
    parser.add_argument(
        "-vip",
        "--vehicle_ip",
        default="127.0.0.1",
        help="IP address to the vehicle interface communication",
    )
    parser.add_argument(
        "-vp",
        "--vehicle_port",
        default="55555",
        help="Port communication to the vehicle",
    )
    parser.add_argument(
        "-s", "--simulation", action="store_true", help="Simulation Mode ON"
    )
    parser.add_argument("-cp", "--config_path", type=str, help="Path to JSON file")

    args = parser.parse_args()

    try:
        # Invoke speech detection
        # speech_to_text()
        if args.simulation:  # Using simulation data
            global simulation
            simulation = args.simulation
            with open(args.config_path) as json_file:
                data = json.load(json_file)

                global sequence
                global sequence_number

                sequence = data["attentive_probability"]
                sequence_number = 0
        else:  # Real data from vehicle
            global client
            client = VSSClient(args.vehicle_ip, args.vehicle_port)
            client.connect()

        # check_drowsiness(85)
        # make_gps_suggestions(52.5170365, 13.3888599)

        listen_to_car(tts)
    except KeyboardInterrupt:
        print("AttentiveAI - application terminated")
        sys.exit()

    print("AttentiveAI -- End of Application")


if __name__ == "__main__":
    run()
