from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from typing import Literal
from TTS.api import TTS
import numpy as np
import soundfile as sf
import torch
import io
import tempfile
import os

# Importa as classes necessárias para a lista de permissões do PyTorch
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import XttsAudioConfig
from TTS.config.shared_configs import BaseDatasetConfig
from TTS.tts.models.xtts import XttsArgs
from TTS.utils.audio import AudioProcessor

# Adiciona todas as classes à lista de permissões do PyTorch.
torch.serialization.add_safe_globals([
    XttsConfig,
    XttsAudioConfig,
    BaseDatasetConfig,
    XttsArgs,
    AudioProcessor
])

app = FastAPI()

@app.post("/create-audio")
async def create_audio(
    text: str,
    language: Literal["en","pt","es"] = "pt",
    voice_to_be_cloned: UploadFile = File(),
    # Adicionando parâmetros de ajuste fino com valores padrão
    temperature: float = 0.7,
    length_penalty: float = 1.2,
    repetition_penalty: float = 2.0,
    top_p: float = 0.9
):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False).to(device)
    
    temp_clone_voice_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            content = await voice_to_be_cloned.read()
            temp_file.write(content)
            temp_clone_voice_path = temp_file.name

        audio = tts.tts(
            text=text,
            speaker_wav=temp_clone_voice_path,
            language=language,
            # Passando os parâmetros ajustáveis para a função tts.tts()
            temperature=temperature, 
            length_penalty=length_penalty, 
            repetition_penalty=repetition_penalty, 
            top_p=top_p
        )
    finally:
        if temp_clone_voice_path and os.path.exists(temp_clone_voice_path):
            os.remove(temp_clone_voice_path)

    audio_array = np.array(audio, dtype=np.float32)
    audio_stream = io.BytesIO()
    
    sf.write(audio_stream, audio_array, samplerate=22050, format='WAV')
    audio_stream.seek(0)
    
    return StreamingResponse(
        audio_stream,
        media_type="audio/wav",
        headers={
            "Content-Disposition": 'attachment; filename="output.wav"'
        }
    )