from pathlib import Path
import os


from utils import stt

file = "data/wenn_der_koennig.wav"

model = stt.get_model("base")
result = stt.transcribe(model=model, file_path=file)
print(f"\nDid you speak {stt.get_language(result)}?")
print()
print("Did you just say:\n\n\t", stt.get_text(result))
print()
