import openai
import asyncio
from telebot.async_telebot import AsyncTeleBot

# masukan api key dari open AI dan api token dari Botfather yang di butuhkan
openai.api_key = "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"
bot = AsyncTeleBot('5535583805:AAH626N8IZwjN2pPnLDfjEVhPZZ8ehDb7wk')


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Halo sayang mau nanya apa?\
""")

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0, max_tokens=1000)
    await bot.reply_to(message, response['choices'][0]['text'])


asyncio.run(bot.polling())