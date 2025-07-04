import os
import uuid
import subprocess
from aiogram import Bot
from aiogram.types import File as TgFile
from config import TEMP_DIR


os.makedirs("temp", exist_ok=True)

async def convert_file(file, bot: Bot):
    tg_file: TgFile = await bot.get_file(file.file_id)

    base_name = str(uuid.uuid4())
    input_path = os.path.join(TEMP_DIR, base_name)
    output_path = os.path.join(TEMP_DIR, base_name + ".wav")

    await bot.download_file(tg_file.file_path, destination=input_path)

    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-vn", "-ac", "1", "-ar", "16000",
        output_path
    ]

    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    os.remove(input_path)

    return output_path
