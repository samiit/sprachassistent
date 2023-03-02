import pyttsx3

from pathlib import Path
import platform

from utils.constants import language_dict


def get_pyttsx3_engine(language: str = "en"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 125)
    if platform.system() == "Linux":
        if language in language_dict:
            engine.setProperty("voice", language_dict[language].lower())
        elif language.title() in language_dict.values():
            engine.setProperty("voice", language.lower())
    return engine


def speak_text(text: str, engine: pyttsx3.Engine):
    engine.say(text)
    engine.runAndWait()


def save_audio(text: str, file_path: Path, engine: pyttsx3.Engine):
    engine.save_to_file(text, file_path)
    engine.runAndWait()
