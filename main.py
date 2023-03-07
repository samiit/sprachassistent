from pathlib import Path


from utils import stt, constants, tts_dl_silero, tts_native

file_audio = "data/wenn_der_koennig.wav"
file_audio_processed = "data/processed/{text}"


def do_stt(file_path: Path):
    model = stt.get_model("base")
    result = stt.transcribe(model=model, file_path=file_path)
    print(f"\nDid you speak {stt.get_language(result)}?")
    print()
    print("Did you just say:\n\n\t", stt.get_text(result))
    print()


def do_tts_dl(text: str, language: str, file_path: Path):
    if language == "en":
        speaker = "lj_16khz"
    elif language == "de":
        speaker = "thorsten_16khz"
    else:
        raise Exception(
            f"Language {constants.language_dict[language]} not supported yet."
        )
    device = tts_dl_silero.get_device()
    model, symbols, sample_rate, apply_tts = tts_dl_silero.get_model_params(
        device, language, speaker
    )
    audio_tensor = tts_dl_silero.get_audio(
        text, model, symbols, sample_rate, apply_tts, device
    )
    tts_dl_silero.write_audio(audio_tensor, sample_rate, file_path)


def do_tts_native(text: str, language: str, file_path: Path):
    engine = tts_native.get_pyttsx3_engine(language=language)
    tts_native.speak_text(text, engine)
    tts_native.save_audio(text, file_path, engine)


def do_tts_native_pico(text: str, language: str, file_path: Path):
    tts_native.save_pico2wave_voice(text, language, file_path)


do_stt(file_path=file_audio)

example_text = """
Mit jedem Atemzug wird mir immer mehr bewußt, 
dass diese Weltvolltrug mir eigentlich zu wieder sein muss.
Doch es ändert sich nicht, egal wie stark mein Wille ist.
Ich schaffe es nicht zu tun, was es normal ist.
"""
do_tts_native(
    example_text,
    language="de",
    file_path=file_audio_processed.format(text="native_example.wav"),
)

do_tts_native_pico(
    example_text,
    language="de",
    file_path=file_audio_processed.format(text="native_pico_example.wav"),
)

do_tts_dl(
    text=example_text,
    language="de",
    file_path=file_audio_processed.format(text="example.wav"),
)
