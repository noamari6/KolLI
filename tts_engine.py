import os
from TTS.api import TTS

# טוען את המודל פעם אחת בלבד
tts_model = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False, gpu=False)

def synthesize(text, voice_path, output_path):
    tts_model.tts_to_file(
        text=text,
        speaker_wav=voice_path,
        language="he",  # עברית
        file_path=output_path
    )
