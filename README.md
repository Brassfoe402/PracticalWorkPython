Телеграмм бот для просмотра новостей https://t.me/News2581_bot

Процесс настройки бота 

Регистрация

Необходимо зарегистрировать и получить уникальный id бота, являющийся одновременно и токеном. Для этого в Telegram существует специальный бот — @BotFather.

Определение переменных окружения

Для работы необходим файл .env в главной директории, в котором будут следующее поле (смотреть файл .env.example):

TOKEN - Телеграм-токен бота

api_key - Токен API

Установка внешних пакетов

Устанавливаем все внешние пакеты из файла requirements.txt:
pip install -r requirements.txt

Для запуска бота используется команда /start

Управление осуществляется через кнопки
