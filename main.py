import logging

from aiogram import Bot, Dispatcher, executor, types

from getNews import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6886947694:AAGezRFdWVm4MOcmwMf3NAKJNOuTtIPRbGY")
dp = Dispatcher(bot)

# Menu keyboard
# Economist, Breaking News, World Events, Politics, Technology, Health, Science, Business, Crypto Stock Market Finance Entertainment Sports Environment Education Lifestyle Travel Culture Weather Crime Social Issues Innovation International Relations Market Trends Art and Design Fashion Food and Dining Human Interest,
menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_keyboard.row("Technology", "AI", "Entertainment")
menu_keyboard.row("Business", 'Sports', 'Music')
menu_keyboard.row('Movies', 'Anime', 'Economist')
menu_keyboard.row('Trending News', 'Blogs', 'Articles')
menu_keyboard.row('Weather', 'Crime', 'Social Issues')
menu_keyboard.row('Innovation', 'International Relations', 'Market Trends')
menu_keyboard.row('Art and Design', 'Fashion', 'Food and Dining')
menu_keyboard.row('Human Interest', 'Breaking News', 'World Events')
menu_keyboard.row('Science', 'Environment', 'Education')
menu_keyboard.row('Lifestyle', 'Travel', 'Culture')
menu_keyboard.row('Crypto', 'Stock Market', 'Finance')



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Hi! I'm News Bot. I can show you the latest news. Select a category from the menu below:", reply_markup=menu_keyboard)

categories = ['Technology', 'Sports', 'Entertainment', 'Business', 'AI', 'Music', 'Movies', 'Anime', 'Economist', 'Crime', 'Social Issues', 'Innovation', 'International Relations', 'Market Trends', 'Art and Design', 'Fashion', 'Food and Dining', 'Human Interest', 'Trending News', 'Blogs', 'Articles', 'Weather', 'Science', 'Environment', 'Education', 'Lifestyle', 'Travel', 'Culture', 'Crypto', 'Stock Market', 'Finance', 'Breaking News', 'World Events']
@dp.message_handler(lambda message: message.text in categories)
async def send_tech_news(message: types.Message):
    await message.reply("Please wait...")
    await bot.send_chat_action(message.chat.id, 'typing')

    titles, bodies, dates, urls = get2daysNews(message.text)

    for i in range(len(titles)):
        if 'hours' in dates[i] or 'hour' in dates[i]:
            if int(dates[i].split()[0]) < 15:
                await message.reply(f"<b>{titles[i]}</b>\n\n<i>{bodies[i]}</i>\n\n{dates[i]}\n\n<a href='{urls[i]}'>Read More</a>", parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)