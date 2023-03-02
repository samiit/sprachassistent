import torch
import torchaudio
from pathlib import Path


def get_device(device: str = "cpu"):
    return torch.device(device)


def get_model_params(
    device: torch.DeviceObjType, language: str = "en", speaker: str = "lj_16khz"
):
    model, symbols, sample_rate, _, apply_tts = torch.hub.load(
        repo_or_dir="snakers4/silero-models",
        model="silero_tts",
        language=language,
        speaker=speaker,
    )
    model = model.to(device)  # gpu or cpu
    return model, symbols, sample_rate, apply_tts


def get_audio(
    text: str, model, symbols, sample_rate, apply_tts, device
) -> torch.Tensor:
    audio = apply_tts(
        texts=[text],
        model=model,
        sample_rate=sample_rate,
        symbols=symbols,
        device=device,
    )
    return audio[0]


def write_audio(audio: torch.tensor, sample_rate: int, file_path: Path):
    torchaudio.save(file_path, audio.reshape(1, -1), sample_rate)
