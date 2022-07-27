from mcstats import mcstats
from aiogram.dispatcher.filters.builtin import Command
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType
from asyncio import sleep
from random import choice

#ip и port сервера
host = "host"
port = 19999

bot = Bot(token="your bot token")
dp = Dispatcher(bot)

#узнаем кол-во играков на сервере
def stat():
    try:
        with mcstats(host, port=port, timeout=5) as data:
            num=(data.__dict__['num_players'])
            stat = str(f"*Mark0bka Server\n     Players:* {num}/10")
            return stat
    except:
        stat = "[Змей](tg://user?id=), [Антон](tg://user?id=) сервер упал и не встает🌚"
        return stat

#сообщение - приветствие
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
    
    #собираем сообщение из списка
    for i in hello_message:
        message += i
    return message

#приветсвуем нового участника
@dp.message_handler(content_types = ["new_chat_members"])
async def new_chat_member(message: types.Message):
    
    #отправляем стикер с Якубовичем
    await message.answer_sticker("CAACAgIAAxkBAAESNJRiPEWNy9Ql-yFsgqeW9lK1wbghaQACdgIAAgk7OxORLH4aUgNjViME")
    sleep(1)
    
    #отправляем сообщение - приветствие
    await message.answer(hello())

#проверяем кол-во играков на сервере
@dp.message_handler(commands='status')
async def main(message: types.Message):
    
    #создаем инлайн-клавиатуру и добавляем кнопку
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Update🔁", callback_data="update"))
    
    #отправляем сообщение с инлайн-клавиатурой
    await message.reply(stat(), parse_mode="Markdown", reply_markup=keyboard)

#обработчик колбеков
@dp.callback_query_handler(text="update")
async def send_random_value(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Update🔁", callback_data="apdate"))
    
    #обновляем информацию при помощи редактирования сообщения
    await call.message.edit_text(stat(), parse_mode="Markdown", reply_markup=keyboard)
    
    await call.answer("Обнoвлено!")

#тоже такая же функция, но только тригерится на другой колбек
#ничего лучше не придумал, для неограниченного кол-во нажатий
#извиняюсь за колхоз
@dp.callback_query_handler(text="apdate")
async def send_random_value1(call: types.CallbackQuery):
    
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Update🔁", callback_data="update"))
    
    await call.message.edit_text(stat(), parse_mode="Markdown", reply_markup=keyboard)
    await call.answer("Обнoвлено!")

#тегаем админов сервера
@dp.message_handler(Command(commands=["admins"]))
async def send_welcome(message: types.Message, command: Command.CommandObj):
    args = command.args
    
    if args == None:
        #говорим юзеру, что нужны аргументы
        await message.answer("Введи сообщение для админов, как показано в образце:\n/admins включите выживание, пожалуйста🥺")
    
    else:
        #тегаем админом и выводим сообщение юзера
        await message.answer(f"[Змей](tg://user?id=), [Антон](tg://user?id=) *{args}*", parse_mode="Markdown")

#файл майнкрафт
@dp.message_handler(commands="minecraft")
async def minecraft(message: types.Message):
    #отправляем скопированное сообщения из чата
    await bot.copy_message(message.chat.id, -10015******71, 179)

#пикча с инфой о спавне руд в 1.18
@dp.message_handler(commands="ores")
async def ores(message: types.Message):
    await bot.copy_message(message.chat.id, -10015******71, 136)

#таблица зельеварения
@dp.message_handler(commands="potions")
async def potions(message: types.Message):
    await bot.copy_message(message.chat.id, -10015******71, 180)

#правила
@dp.message_handler(commands="rules")
async def rules(message: types.Message):
    await message.answer(hello())

#прощаемся с вышедшим юзером
@dp.message_handler(content_types = types.ContentTypes.LEFT_CHAT_MEMBER)
async def left_chat_members(message: types.Message):
    
    #грустный стикер с Якубовичем
    await bot.copy_message(message.chat.id, -10015******71, 343)

#запускаем бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)