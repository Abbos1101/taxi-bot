
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
import asyncio
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = "7519441498:AAFzzl7yplK1nfjaAudbl8Sa-Mxi-cW8Qjg"
DRIVER_GROUP_ID = -4960701216  # Haydovchilar guruhi ID si
ADMIN_ID = 6128106930  # Admin Telegram ID si

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

user_data = {}

# MySQL ulanish
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABAS_
