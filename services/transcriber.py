import whisper

model = whisper.load_model("medium")

def transcribe(path_to_wav: str):
    result = model.transcribe(path_to_wav, beam_size=5, fp16=False)
    return result["text"]