from aiogram import Router, F
from aiogram.types import Message
from config import Max_File_Size_MB, Max_Duration_Minutes

media_route = Router()


@media_route.message(F.voice | F.audio | F.video)
async def media_handler(message: Message):
    file = (message.voice or message.video or message.audio)

    if not file:
        await message.answer("Не удалось определить файл.")
        return

    if file.file_size > Max_File_Size_MB * 1024 * 1024:
        await message.answer("Файл слишком большой.")

    if file.duration > Max_Duration_Minutes * 60:
        await message.answer("Файл слишком долгий.")

    await message.answer("Файл получен. Начинаю обработку...")

    try:

        text = "Какой-то текст"

        if text.strip():
            await message.answer(text)
        else:
            await message.answer("Не удалось распознать речь.")
    except Exception as e:
        await message.answer(str(e))
