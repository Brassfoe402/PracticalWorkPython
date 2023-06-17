import telebot
from newsapi import NewsApiClient
from GoogleNews import GoogleNews
import random
import os

bot = telebot.TeleBot('6181407907:AAGMhYmhmQyZV1bUpsbJ40fVJJ-29GVU1WI')
newsapi = NewsApiClient(api_key='79a94d6eae0a4829adfc9c839f157bb1')
googlenews = GoogleNews(lang='ru')

# функция, которая отправляет сообщение с кнопками
def send_categories(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    markup.add('Технологии', 'Политика', 'Здоровье', 'Развлечения', 'Общее', 'Война', 'Наука', 'Спорт', 'Землетрясения', 'Вселенная', 'Растения', 'Оружие')

    bot.send_message(message.chat.id, 'Выберите категорию новостей:', reply_markup=markup)

# функция для обработки команды старта
@bot.message_handler(commands=['start'])
def start_handler(message):
    send_categories(message)

# функция для получения новостей по теме
@bot.message_handler(func=lambda message: True)
def news_handler(message):
    topic = message.text

    # получаем новости с помощью сервиса newsapi
    headlines = newsapi.get_top_headlines(q=topic, language='ru', page_size=5)

    if headlines is not None and headlines['status'] == 'ok' and headlines['totalResults'] > 0:
        for article in headlines['articles']:
            bot.send_message(message.chat.id, article['title'])
            bot.send_message(message.chat.id, article['url'])
    else:
        # если новости не найдены на newsapi, ищем на Google News
        googlenews.search(topic)
        for res in googlenews.results()[:5]:
            bot.send_message(message.chat.id, res['title'])
            bot.send_message(message.chat.id, res['link'])

# обработчики категорий
@bot.message_handler(func=lambda message: message.text == 'Технологии')
def technology_handler(message):
    articles = newsapi.get_top_headlines(category='technology', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)

# обработчик для категории "Политика"
@bot.message_handler(func=lambda message: message.text == 'Политика')
def politics_handler(message):
    articles = newsapi.get_top_headlines(category='politics', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)

# обработчик для категории "Здоровье"
@bot.message_handler(func=lambda message: message.text == 'Здоровье')
def health_handler(message):
    articles = newsapi.get_top_headlines(category='health', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)
# обработчик для категории "Общество"
@bot.message_handler(func=lambda message: message.text == 'Общее')
def general_handler(message):
    articles = newsapi.get_top_headlines(category='general', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)

# обработчик для категории "Война"
@bot.message_handler(func=lambda message: message.text == 'Война')
def war_handler(message):
     articles = newsapi.get_top_headlines(category='war', language='ru', page_size=100)
     if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
     else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
     send_categories(message)

# обработчик для категории "Развлечения"
@bot.message_handler(func=lambda message: message.text == 'Развлечения')
def entertainment_handler(message):
    articles = newsapi.get_top_headlines(category='entertainment', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)

# обработчик для категории "Наука"
@bot.message_handler(func=lambda message: message.text == 'Наука')
def science_handler(message):
    articles = newsapi.get_top_headlines(category='science', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)

# обработчик для категории "Спорт"
@bot.message_handler(func=lambda message: message.text == 'Спорт')
def sports_handler(message):
    articles = newsapi.get_top_headlines(category='sports', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)

# обработчик для категории "Землетрясения"
@bot.message_handler(func=lambda message: message.text == 'Землетрясения')
def earthquakes_handler(message):
    articles = newsapi.get_top_headlines(category='earthquakes', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)

# обработчик для категории "Вселенная"
@bot.message_handler(func=lambda message: message.text == 'Вселенная')
def universe_handler(message):
    articles = newsapi.get_top_headlines(category='universe', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)

# обработчик для категории "Растения"
@bot.message_handler(func=lambda message: message.text == 'Растения')
def plants_handler(message):
    articles = newsapi.get_top_headlines(category='plants', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)

# обработчик для категории "Оружие"
@bot.message_handler(func=lambda message: message.text == 'Оружие')
def weapon_handler(message):
    articles = newsapi.get_top_headlines(category='weapon', language='ru', page_size=100)
    if len(articles) > 0:
        article = random.choice(articles)
        bot.send_message(message.chat.id, article['title'])
        bot.send_message(message.chat.id, article['url'])
        bot.delete_message(message.chat.id, message.id)
        send_categories(message)
    else:
        bot.send_message(message.chat.id, 'К сожалению, для данной категории не найдены новости.')
    send_categories(message)
# запуск бота
bot.polling(none_stop=True)
