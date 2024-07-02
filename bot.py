import os
from asyncio import run
from aiogram import F
from aiogram.types import Message , BotCommand
from dotenv import load_dotenv
from aiogram.filters import Command , CommandStart
from functions import start , echo, stop , start_menu,share_menu,register_contact,register_location,check_join
from functions import start,stop,check_join
from filters import CheckSubFilter
from keyboards import channel_list
from filters import CheckSubFilter


#
load_dotenv()
#
from aiogram import Bot , Dispatcher
#
TOKEN = os.getenv("BOT_TOKEN")
#
#

dp = Dispatcher()


# bu hamasi register qlish uchun
async def main(dp) -> None:
    bot = Bot(token=TOKEN,skip_updates=True)
    await bot.set_my_commands(

        [
            BotCommand(command="/start" , description="Bot ni ishga tushrish"),
            BotCommand(command="/help" , description="Yordam"),
            BotCommand(command="/share", description="Malumotlarni junatish")
        ]
    )
    dp.startup.register(start)
    dp.message.register(check_join,CheckSubFilter()) # bu funksiya kanalga azo bulish ujun register qlingan
    dp.callback_query.register(check_channel_join,F.data=="check_subscription") # bu kanalga ozo bugan ili yoqligini kurop kegin bzaga jovop beradi registerniki
    dp.message.register(start_menu , CommandStart())
    dp.message.register(share_menu , Command('share'))
    dp.message.register(register_location , F.location)
    dp.message.register(register_contact , F.contact)
    dp.message.register(echo)
    dp.shutdown.register(stop)
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main(dp))

