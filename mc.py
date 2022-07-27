from mcstats import mcstats
from aiogram.dispatcher.filters.builtin import Command
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from asyncio import sleep
from datetime import datetime as dt
from random import choice

host = "mint.mcpehost.ru"
port = 19999

bot = Bot(token="5208615210:AAFRLT865o9oMPnkbL0pgou9xPTsjvi1UEs")
dp = Dispatcher(bot)

first_time = dt.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")


def stat():
    try:
        with mcstats(host, port=port, timeout=5) as data:
            num=(data.__dict__['num_players'])
            stat = str(f"*Mark0bka Server\n     Players:* {num}/10")
            return stat
    except:
        stat = "[Змей](tg://user?id=809901505), [Антон](tg://user?id=1123543137) сервер упал и не встает🌚"
        return stat

def hello():
    
    message = ""
    
    hello_message = [
        "Правила:\n👉 Спавн и все на нем общее (радиус от точки спавна -3159 1260 - 50 кубов)",
        "\n⛺️ Строишь дом - делай таблички.\n🕋 Поставил сундук - поставь и табличку.\n📝 Все подписываем табличками.\n🏡 Все что в доме или огорожено вокруг дома и подписано - приватное.",
        "\n📬 Сделайте почту: бочку или сундук с табличкой подписанной тэгом учетной записи, помогает в обмене.\n🌍 Напишите в чат координаты своего дома или землянки, чтобы можно было собрать вечеринку друзей или прийти на помощь.",
        "\n🤲 Ходить, спать в кроватях и рыться в сундуках - можно. Брать что либо нельзя.\n✏️ Предметы можно переименовывать в наковальне своим ником, чтобы в случае потери понятно было чей шмот.",
        "\n🗃 В качестве сейфа для особо ценного лута идеально подходит Эндер сундук с шалкерами внутри. Их много стоит у всех. Я ставлю даже у почты сундук.\n🐷🐮🐶🐱🐔 Соответственно животные и огороды в загонах у дома - приватные.",
        "\n🌳🌲🌴 Береги природу — мать твою! Срубил дерево - посади новое из саженца, не делаем ебучих столбов, стараемся освещать территорию.\n🌚 Сервер приватный, мы все тут в принципе друг другу друзья.",
        "\n💥 Поскольку криперы ща ебашат сильнее, если вы сломали чужую постройку крипером - вы должны ее починить.\n🪓🚫 За угрозы и слова в инете карают не только в РФ, но и на нашем сервере. Не надо обещать устроить лаги, дюп-машины и прочие вещи, способные поломать сервер.",
        "\n🔥 Читы тоже под запретом. Даже текстурпаки и ресурс паки с компасом. (Используйте карту, я постараюсь всем выдать карты 🗺 )",
        "\n😈👹👺 Для быстрого перемещения используем АД. Высота постойки всех порталов в аду к вашим домам - 100 блоков. На этой высоте простраиваем все дороги в аду.",
        "\n🚷 Если Антон увидит, что кто-то роется в его сундуках без его согласия, он имеет полное право убить этого человека ♿️ , ограничить ему доступ к сундукам и редстоуну и забрать себе его ресурсы. Змей сделает тоже самое. Честно говоря ситуации с гриферами немного надоели."
        "\n🙋‍♂ Всем новичкам нужно подписаться на этот новостной канал, а еще пообещать выполнять данные правила, являющиеся социальным договором на нашем сервере.",
        "\n\nЕсли надо что - спроси в чатике. Всегда поделимся ресами или подскажем куда идти за ними."
    ]
    
    for i in hello_message:
        message += i
    
    return message

@dp.message_handler(content_types = ["new_chat_members"])
async def new_chat_member(message: types.Message):
    
    await message.answer_sticker("CAACAgIAAxkBAAESNJRiPEWNy9Ql-yFsgqeW9lK1wbghaQACdgIAAgk7OxORLH4aUgNjViME")
    sleep(1)
    await message.answer(hello())

@dp.message_handler(commands='status')
async def main(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Update🔁", callback_data="update"))
    await message.reply(stat(), parse_mode="Markdown", reply_markup=keyboard)

@dp.callback_query_handler(text="update")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Update🔁", callback_data="apdate"))
    await call.message.edit_text(stat(), parse_mode="Markdown", reply_markup=keyboard)
    await call.answer("Обнoвлено!")

@dp.callback_query_handler(text="apdate")
async def send_random_value1(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Update🔁", callback_data="update"))
    await call.message.edit_text(stat(), parse_mode="Markdown", reply_markup=keyboard)
    await call.answer("Обнoвлено!")

@dp.message_handler(Command(commands=["admins"]))
async def send_welcome(message: types.Message, command: Command.CommandObj):
    args = command.args
    if args == None:
        await message.answer("Введи сообщение для админов, как показано в образце:\n/admins включите выживание, пожалуйста🥺")
    else:
        await message.answer(f"[Змей](tg://user?id=809901505), [Антон](tg://user?id=1123543137) *{args}*", parse_mode="Markdown")
    
@dp.callback_query_handler(text="yes")
async def yes(call: types.CallbackQuery):
    global first_time
    result = dt.now() - first_time
    if result.seconds > 180:
        first_time = dt.now()
        await call.message.edit_text('[Змей](tg://user?id=809901505), [Антон](tg://user?id=1123543137) вы нам нужны👀', parse_mode="Markdown")
    else:
        ostatok = 180 - result.seconds #я просто не знал, как будет на английском "остаток")))
        await call.answer(f'Попробуй снова через {ostatok // 60}m {ostatok % 60}s')

@dp.callback_query_handler(text="no")
async def no(call: types.CallbackQuery):
    await call.answer("ok")
    await call.message.delete()

@dp.message_handler(commands="minecraft")
async def minecraft(message: types.Message):
    await bot.copy_message(message.chat.id, -1001528440871, 179)

@dp.message_handler(commands="ores")
async def ores(message: types.Message):
    await bot.copy_message(message.chat.id, -1001528440871, 136)

@dp.message_handler(commands="potions")
async def potions(message: types.Message):
    await bot.copy_message(message.chat.id, -1001528440871, 180)

@dp.message_handler(commands="rules")
async def rules(message: types.Message):
    await message.answer(hello())

@dp.message_handler(content_types = types.ContentTypes.LEFT_CHAT_MEMBER)
async def left_chat_members(message: types.Message):
    await bot.copy_message(message.chat.id, -1001528440871, 343)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)