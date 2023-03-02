import pyttsx3

from pathlib import Path
import platform
import os

from utils.constants import language_dict, pico_language_dict


def get_pyttsx3_engine(language: str = "en"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 125)
    if platform.system() == "Linux":
        if language in language_dict:
            lang = language_dict[language].lower()
        elif language.title() in language_dict.values():
            lang = language.lower()
        engine.setProperty("voice", lang)
    return engine


def speak_text(text: str, engine: pyttsx3.Engine):
    engine.say(text)
    engine.runAndWait()


def save_audio(text: str, file_path: Path, engine: pyttsx3.Engine):
    engine.save_to_file(text, file_path)
    engine.runAndWait()


def save_pico2wave_voice(text: str, language: str, file_path: Path):
    if platform.system() != "Linux":
        raise Exception("This function does not work on your Operating System.")

    if language in pico_language_dict.values():
        lang = language
    elif language in language_dict:
        if language in pico_language_dict:
            lang = pico_language_dict[language]
        else:
            raise Exception("Language not supported")
    elif language in language_dict.values():
        lang_code = [l for l in language_dict if language_dict[l] == language][0]
        if lang_code in pico_language_dict:
            lang = pico_language_dict[lang_code]
        else:
            raise Exception("Language not supported")
    else:
        raise Exception("Language not supported")
    os.system(f"pico2wave -l={lang} -w={file_path} '{text}'")
