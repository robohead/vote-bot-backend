# Vote-bot

[![Build Status](https://travis-ci.org/Iamthelaw/vote-bot.svg?branch=master)](https://travis-ci.org/Iamthelaw/vote-bot)
[![Join the chat at https://gitter.im/Iamthelaw/vote-bot](https://badges.gitter.im/Iamthelaw/vote-bot.svg)](https://gitter.im/Iamthelaw/vote-bot?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Slack-бот для голосований

## Список поддерживаемых команд
- `/vote, /vote help`
- `/vote add [text]` добавить предложение для голосования
- `/vote update [id] [text]` обновить текст предложения (только автор)
- `/vote delete [id]` удалить предложение для голосования
- `/vote rate [id] [1-5]` оценить предложение для голосования
- `/vote show [id]` показать детальную информацию о преложении для голосования
- `/vote list` список всех предложений

## Веб-интерфейс
- `YOURDOMAIN/` входная точка для шаблона index.html
- `YOURDOMAIN/api` апи для получения списка предложений для голосования

## Установка
1. `$ pip install -r requirements.txt`
2. `$ echo "SLACK_TOKEN='' SLASH_COMMANDS_TOKEN='' DOMAIN='' DEFAULT_CHANNEL='' python app.py" > start.sh`
3. `$ chmod +x start.sh && ./start.sh`

## Build Setup

``` bash
# Установка зависимостей
npm install

# Запуск сервера с hot reload по адресу localhost:8080
npm run dev

# Продакшен сборка
npm run build
```

В сборке используется шаблон [webpack-simple](https://github.com/vuejs-templates/webpack-simple).
