from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

user_languages = {}

language_router = Router()

LANGUAGE_MAP = {
    "ru": "Русский 🇷🇺",
    "en": "English 🇬🇧",
}


@language_router.message(F.text == "/language")
async def choose_language(message: Message):
    builder = InlineKeyboardBuilder()
    for code, name in LANGUAGE_MAP.items():
        builder.button(text=name, callback_data=f"set_lang:{code}")
    keyboard = builder.as_markup()
    await message.answer("Выберите язык распознавания:", reply_markup=keyboard)


@language_router.callback_query(F.data.startswith("set_lang:"))
async def set_language(callback: CallbackQuery):
    lang_code = callback.data.split(":")[1]
    user_languages[callback.from_user.id] = lang_code
    await callback.answer(f"Язык установлен: {LANGUAGE_MAP[lang_code]}")
    await callback.message.edit_text(f"Выбран язык: {LANGUAGE_MAP[lang_code]}")
