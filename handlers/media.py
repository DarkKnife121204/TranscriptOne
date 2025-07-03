import logging

from aiogram import Router, F
from aiogram.types import Message
from config import Max_File_Size_MB, Max_Duration_Minutes

from services.file import convert_file
from services.transcriber import transcribe

Supported_types ={
    "audio/mpeg",
    "audio/x-wav",
    "audio/wav",
    "audio/ogg",
    "audio/mp4",
    "video/mp4",
    "video/quicktime",
    "video/x-msvideo"
}

media_route = Router()


@media_route.message(F.voice | F.audio | F.video)
async def media_handler(message: Message):
    file = (message.voice or message.video or message.audio)

    if file.file_size > Max_File_Size_MB * 1024 * 1024:
        await message.answer("Файл слишком большой.")
        return

    if file.duration > Max_Duration_Minutes * 60:
        await message.answer("Файл слишком долгий.")
        return

    if file.mime_type not in Supported_types:
        await message.answer("Неверный тип файла.")
        return

    await message.answer("Файл получен. Начинаю обработку...")
    logging.info(f"[{message.from_user.id}] Загружен файл: {file.file_id}")

    await message.answer(f"Примерное время обработки: {file.duration:} сек.")
    logging.info(f"[{message.from_user.id}] Примерное время обработки: {file.duration:} сек.")

    try:
        logging.info(f"[{message.from_user.id}] Извлечение звука из файла начато")
        local_wav = await convert_file(file, message.bot)
        logging.info(f"[{message.from_user.id}] Звук извлечён, путь: {local_wav}")

        logging.info(f"[{message.from_user.id}] Начата транскрибация")
        text = await transcribe(local_wav, message.from_user.id)
        logging.info(f"[{message.from_user.id}] Транскрибация завершена")

        if text.strip():
            await message.answer(text)
        else:
            await message.answer("Не удалось распознать речь.")
    except Exception as e:
        logging.exception(f"[{message.from_user.id}] Ошибка при обработке файла: {e}")
        await message.answer(str(e))
