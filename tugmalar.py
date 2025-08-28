# tugmalar.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# Asosiy menyu
menyu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Katalog', callback_data='catalog')
    ]
])

# Katalog tugmalari
inline_katalog = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Yoz fasli", callback_data='yoz')
    ],    
    [
        InlineKeyboardButton(text="Qish fasli", callback_data='qish')
    ]
])

yoz = InlineKeyboardMarkup(inline_keyboard=[

    [
        InlineKeyboardButton(text="Antalya (Turkiya)", callback_data='antalya')
    ],

    [
        InlineKeyboardButton(text="Bali (Indoneziya)", callback_data='bali')
    ],

    [
        InlineKeyboardButton(text="Maldive orollari", callback_data='maldive')
    ],

    [
        InlineKeyboardButton(text="Dubay (Birlashgan Arab Amirliklari)", callback_data='dubai')
    ],

    [
        InlineKeyboardButton(text="Santorini (Gretsiya)", callback_data='santoroni')
    ],

    [
        InlineKeyboardButton(text="Bangkok (Tailand)", callback_data='bangkok')
    ],

    [
        InlineKeyboardButton(text="Barselona (Ispaniya)", callback_data='barselona')
    ],

    [
        InlineKeyboardButton(text="Dubrovnik (Xorvatiya)", callback_data='dubrovnik')
    ],

    [
        InlineKeyboardButton(text="Kuba (Gavana)", callback_data='kuba')
    ],

    [
        InlineKeyboardButton(text="Jeju oroli (Janubiy Koreya)", callback_data='jeju')
    ]

])

qish = InlineKeyboardMarkup(inline_keyboard=[

    [
        InlineKeyboardButton(text="Alplar (Shveytsariya, Avstriya, Italiya, Fransiya)", callback_data='Alplar')
    ],

    [
        InlineKeyboardButton(text="Tromsø (Norvegiya)", callback_data='Tromso')
    ],

    [
        InlineKeyboardButton(text="Islandiya", callback_data='Islandiya')
    ],

    [
        InlineKeyboardButton(text="Laplandiya (Finlyandiya)", callback_data='Laplandiya')
    ],

    [
        InlineKeyboardButton(text="Seul (Janubiy Koreya)", callback_data='Seul')
    ],

    [
        InlineKeyboardButton(text="Tokio (Yaponiya)", callback_data='Tokio')
    ],

    [
        InlineKeyboardButton(text="New York (AQSH)", callback_data='New York')
    ],

    [
        InlineKeyboardButton(text="Moskva (Rossiya)", callback_data='Moskva')
    ],

    [
        InlineKeyboardButton(text="Vena (Avstriya)", callback_data='Vena')
    ],

    [
        InlineKeyboardButton(text="Praga (Chexiya)", callback_data='Praga (Chexiya)')
    ]

])

# Orqaga qaytish tugmasi (faqat katalogga)
orqaga = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Orqaga', callback_data='orqaga')
    ]
])

# Orqaga va bosh sahifa tugmalari
orqaga_va_bosh = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Orqaga', callback_data='orqaga'),
        InlineKeyboardButton(text='Bosh sahifa', callback_data='bosh_sahifa')
    ]
])

# Bosh sahifa tugmasi
bosh_sahifa = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Bosh sahifa', callback_data='bosh_sahifa')
    ]
])


# phone_button = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='Telefon raqamni yuborish', request_contact=True)
#         ]
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=True
# )
