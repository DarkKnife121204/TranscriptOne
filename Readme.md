# TranscriptOne — Telegram бот для расшифровки аудио и видео

---

##  Возможности

- Расшифровка **аудио** и **видео** в текст
- Поддержка форматов: `.mp3`, `.wav`, `.ogg`, `.m4a`, `.mp4`, `.mov`, `.avi`
- Поддержка **голосовых сообщений**
- Выбор языка распознавания через команду `/language`
- Офлайн работа через `openai-whisper`
- Docker
- Подсчёт примерного времени обработки

---

## Установка и запуск

Токен Telegram-бота указывается в файле `config.py` в переменной `Token`.

Перед установкой и запуском требуется запущенный Docker

```bash
git clone https://github.com/yourusername/transcriber-bot.git
cd transcriber-bot
docker build -t transcriber-bot .
docker run --name transcriber-bot-container transcriber-bot
```