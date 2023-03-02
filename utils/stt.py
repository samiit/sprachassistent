import whisper
from pathlib import Path

from utils.constants import language_dict


def get_model(model_name: str) -> whisper.Whisper:
    return whisper.load_model(model_name)


def transcribe(model: whisper.Whisper, file_path: Path) -> dict:
    return model.transcribe(file_path)


def get_language(transcipt: dict) -> str:
    return language_dict[transcipt["language"]]


def get_text(transcipt: dict) -> str:
    return transcipt["text"]
