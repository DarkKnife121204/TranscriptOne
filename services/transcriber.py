import whisper
import asyncio
from handlers.language import user_languages

model = whisper.load_model("medium")


def _transcribe_sync(model, path_to_wav, language):
    return model.transcribe(path_to_wav, beam_size=1, fp16=False, language=language)


async def transcribe(path_to_wav, user_id):
    language = user_languages.get(user_id, "ru")
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, _transcribe_sync, model, path_to_wav, language)
    return result["text"]
