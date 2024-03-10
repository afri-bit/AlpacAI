"""Synthesizes speech from the input string of text."""

import pyttsx3


class TextToSpeech:

    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 175)

    def text_to_speech(self, txt):
        """Generates audio content for given text

        Args:
            txt (str): Text to be voiced
        """

        self.engine.say(txt)
        self.engine.runAndWait()
