from pathlib import Path
import os


from utils import stt, tts, constants

file_audio = "data/wenn_der_koennig.wav"
file_audio_processed = "data/processed/{text}"


def do_stt(file_path: Path):
    model = stt.get_model("base")
    result = stt.transcribe(model=model, file_path=file_path)
    print(f"\nDid you speak {stt.get_language(result)}?")
    print()
    print("Did you just say:\n\n\t", stt.get_text(result))
    print()


def do_tts(text: str, language: str, file_path: Path):
    if language == "en":
        speaker = "lj_16khz"
    elif language == "de":
        speaker = "thorsten_16khz"
    else:
        raise Exception(
            f"Language {constants.language_dict[language]} not supported yet."
        )
    device = tts.get_device()
    model, symbols, sample_rate, apply_tts = tts.get_model_params(
        device, language, speaker
    )
    audio_tensor = tts.get_audio(text, model, symbols, sample_rate, apply_tts, device)
    tts.write_audio(audio_tensor, sample_rate, file_path)


do_stt(file_path=file_audio)

example_text = "In deinem Haus bin ich gern Vater."
do_tts(
    text=example_text,
    language="de",
    file_path=file_audio_processed.format(text="example.wav"),
)
