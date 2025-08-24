# run.py
import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from tugmalar import *
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 1-Handler - Start komandasi
# print("Bu yangi commit uchun!")
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Assalomu alaykum hurmatli foydalanuvchi!\nTest Botimizga xush kelibsiz!\nSiz bu yerdan toz faslida va qish faslida qayerga sayohat qilishni tanlashingiz mumkin!", 
                        reply_markup=menyu)
                        

# 2-Handler - Katalog tugmasi
@dp.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer("Siz Katalog tugmasini bosdingiz!")
    await callback.message.edit_text('Siz qaysi faslda sayohay qilmoqchisiz?:', reply_markup=inline_katalog)


# 4-Handler - Anor haqida
@dp.callback_query(F.data == 'yoz')
async def yoz_info(callback: CallbackQuery):
    await callback.answer("Yozda sayohat qilish uchun mamlakatlar!")
    yoz_text = yoz
    await callback.message.edit_text(yoz_text, reply_markup=orqaga_va_bosh)

# 5-Handler - Olma haqida
@dp.callback_query(F.data == 'olma')
async def olma_info(callback: CallbackQuery):
    await callback.answer("Olma haqida ma'lumot!")
    olma_text = """
OLMA HAQIDA MA'LUMOT

Olma (lotincha: Malus domestica) — guldoshlar oilasiga mansub daraxt mevasi.

Foydali xususiyatlari:
• Tolalar (fiber) bilan boy
• Vitamin C manbai
• Antioksidantlar mavjud
• Xolesterol darajasini kamaytiradi

Iste'mol qilish usullari:
• Xom holda iste'mol
• Pishirish uchun
• Sharbat tayyorlash
• Quritilgan olma

Mavsumi: Avgustdan noyabrgacha
    """
    await callback.message.edit_text(olma_text, reply_markup=orqaga_va_bosh)

# 6-Handler - Anjir haqida
@dp.callback_query(F.data == 'anjir')
async def anjir_info(callback: CallbackQuery):
    await callback.answer("Anjir haqida ma'lumot!")
    anjir_text = """
ANJIR HAQIDA MA'LUMOT

Anjir (lotincha: Ficus carica) — tut oilasiga mansub o'simlik mevasi.

Foydali xususiyatlari:
• Tolalar bilan juda boy
• Kaliy va magniy manbai
• Tabiiy shakar mavjud
• Suyak salomatligi uchun foydali

Iste'mol qilish usullari:
• Yangi anjir
• Quritilgan anjir
• Murabbo tayyorlash
• Shirinliklar uchun

Mavsumi: Iyuldan oktabrgacha

Anjir qadimgi zamonlardan beri O'rta er dengizi hududlarida yetishtiriladi.
    """
    await callback.message.edit_text(anjir_text, reply_markup=orqaga_va_bosh)

# 7-Handler - Banan haqida
@dp.callback_query(F.data == 'banan')
async def banan_info(callback: CallbackQuery):
    await callback.answer("Banan haqida ma'lumot!")
    banan_text = """
BANAN HAQIDA MA'LUMOT

Banan (lotincha: Musa) — banan oilasiga mansub tropik o'simlik mevasi.

Foydali xususiyatlari:
• Kaliy bilan juda boy
• Vitamin B6 manbai
• Tabiiy energiya beruvchi
• Sportchilar uchun ideal

Iste'mol qilish usullari:
• Xom holda iste'mol
• Smoodi tayyorlash
• Pishiriq uchun
• Quritilgan chips

Mavjudligi: Yil davomida

Banan tropik va subtropik hududlarda yetishtiriladi va dunyoning eng mashhur mevalaridan biri.
    """
    await callback.message.edit_text(banan_text, reply_markup=orqaga_va_bosh)

# 8-Handler - Uzum haqida
@dp.callback_query(F.data == 'uzum')
async def uzum_info(callback: CallbackQuery):
    await callback.answer("Uzum haqida ma'lumot!")
    uzum_text = """
UZUM HAQIDA MA'LUMOT

Uzum (lotincha: Vitis vinifera) — uzum oilasiga mansub o'simlik mevasi.

Foydali xususiyatlari:
• Antioksidantlar (resveratrol) bilan boy
• Vitamin C va K mavjud
• Yurak salomatligi uchun foydali
• Xotira yaxshilaydi

Iste'mol qilish usullari:
• Yangi uzum
• Quritilgan uzum (mayiz)
• Sharbat tayyorlash
• Vino ishlab chiqarish

Mavsumi: Avgustdan oktabrgacha

Uzum qadimgi zamonlardan beri dunyoning turli hududlarida yetishtiriladi va vino ishlab chiqarish uchun ishlatiladi.
    """
    await callback.message.edit_text(uzum_text, reply_markup=orqaga_va_bosh)

# 9-Handler - Orqaga qaytish (katalogga)
@dp.callback_query(F.data.in_(['orqaga', 'back']))
async def orqaga_katalog(callback: CallbackQuery):
    await callback.answer("Katalogga qaytildi!")
    await callback.message.edit_text('Bitta meva tanlang:', reply_markup=inline_katalog)

# 10-Handler - Bosh sahifaga qaytish
@dp.callback_query(F.data == 'bosh_sahifa')
async def bosh_sahifa_handler(callback: CallbackQuery):
    await callback.answer("Bosh sahifaga qaytildi!")
    await callback.message.edit_text(f"Assalomu alaykum hurmatli foydalanuvchi!\nTest Botimizga xush kelibsiz!", 
    reply_markup=menyu)



async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Dastur to'xtadi!")