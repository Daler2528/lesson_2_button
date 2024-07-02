import os
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message , BotCommand , CallbackQuery
from keyboards import menu_button ,location_contact_button
from keyboards import channel_list
from pathlib import Path
import aiofiles as aiof
from tempfile import gettempdir

tmp_filename = Path(__file__).parent/"user.txt"

#bu esa userga Buttonlarni chqarip beradi
async def start_menu(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Menyulardan brini tanlang", reply_markup=menu_button)

#bu esa userga Buttonlarni chqarip beradi
async def share_menu(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Menyulardan brini tanlang", reply_markup=location_contact_button)

#Bu esa lokatsiyani qbil qladi
async def register_location(message: Message, bot: Bot, state: FSMContext):
    print(message.location.latitude , message.location.longitude)
    await bot.send_location(chat_id="5754977794" , latitude=message.location.latitude , longitude=message.location.longitude)
    await message.answer(text="Sizni lotaksiyangiz qabul qlindi tez orada yetqazip beramiz")

#Bu esa kontaktni qbil qladi
async def register_contact(message: Message, bot: Bot, state: FSMContext):
    await bot.send_contact(chat_id="5754977794",phone_number=message.contact.phone_number,first_name=message.contact.first_name)
    await message.answer(text="sizni raqamingizni qabul qilding tez orada aloqa chqamiza")

#bu esa kanalni silKASINI JUNATADI
async def check_join(message: Message, bot: Bot, state: FSMContext):
   await message.answer("Botimizdan foydanishiz uchun <a href='https://t.me/+TEZMzGe03nMyODUy'> Python_24 </a>ga a'zo bo'ling" , parse_mode="html")

#bu esa kanalni silKASINI JUNATADI bu inlien buttoniki
async def check_join(message: Message, bot: Bot, state: FSMContext):
   # await write_user(chad_id=message.from_user.id,first_name=message.from_user.first_name) # bu esa write_userni ishga tushrip bza ismo blan id ni olip bradi
    await message.answer("Botimizdan foydanishiz uchun kanalarga azo buling" , reply_markup=channel_list)

#bu esa kanalga azo bulgan ili yoqligini kurp bzaga jovop beradi
async def check_channel_join(query: CallbackQuery,bot:Bot,*args,**kwargs):
    await bot.send_message(chat_id=query.from_user.id , text="Botmizga Xush kelipsiz")
    await query.answer("")


async def write_user(chad_id ,first_name):
    async with aiof.open(tmp_filename , 'a' , encoding="utf-8") as out:
        await out.write(f"User_id{chad_id} , Firstname{first_name} \n")
        await out.flush()
    print("Done")



#bu esa yozgan malumotlarimini userni uziga junatadi
async def echo(message: Message, bot: Bot, state: FSMContext):
    await message.copy_to(chat_id=message.from_user.id, message=message)

#bu Bot esa  ishga tushkani bildradi
async def start(bot: Bot):
    await bot.send_message(chat_id="5754977794" , text = "Bot ishga tushdi ✅")

# bu Bot esa tuxtaganin bildradi bildradi
async def stop(bot: Bot):
    await bot.send_message(chat_id="5754977794" , text = "Bot Tuxtadi ❌")





