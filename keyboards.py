from aiogram.types import ReplyKeyboardMarkup , KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


#bu esa buttonlarni yaratish uchun -> BUTTON
menu_button = ReplyKeyboardMarkup(keyboard=
    [
        [KeyboardButton(text="Button-1") , KeyboardButton(text="Button-2")],
        [KeyboardButton(text="Button-3") , KeyboardButton(text="Button-4")],
    ],
    resize_keyboard=True
)

location_contact_button = ReplyKeyboardMarkup(keyboard=
   [
       [
           KeyboardButton(text="Lokatsiya junatish" , request_location=True),
           KeyboardButton(text="Kontakni junatish" , request_contact=True)
       ]
   ],
resize_keyboard=True
)

#Inlaeni keyboed bu buttoni boshqachasi

channel_list = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Obuna bo'ling" , url='https://t.me/+ClZKu_QMDNM3MDky'),
            InlineKeyboardButton(text="➕ Obuna bo'ling" , url='https://t.me/sherzotvich_ss'),
            InlineKeyboardButton(text="➕ Obuna bo'ling" , url='https://www.instagram.com/nasimov_2528?igsh=YmhsdWNxOWFpNmF')
        ],
        [
            InlineKeyboardButton(text="Tekshrish ✅" , callback_data="check_subscription"),

        ]
    ]
)




