#Owned By @TheKaizuryu & @Xelcius

from telethon import events, Button, custom
import re, os
from ShogunXRobot.events import register
from ShogunXRobot import telethn as tbot
from ShogunXRobot import telethn as tgbot
PHOTO = "https://telegra.ph/file/d9c46e3db8952c020256b.jpg"
@register(pattern=("/alive"))
async def awake(event):
  Raiden = f"**剣 Hii {event.sender.first_name} I'm Raiden Sword** \n\n"
  Raiden += "**剣 I'm Property OF @AogiriNetwork**\n\n"
  Raiden += "**剣 Raiden Shogun 剣: Sword Master Version **\n\n"
  Raiden += "**剣 Creator:** [Ryomen Sukuna](t.me/Xelcius)\n\n"
  Raiden += "**剣 python-Telegram-Bot: 13.11**\n\n"
  BUTTON = [[Button.url("Support", "https://t.me/Scythe_Support"), Button.url("Updates", "https://t.me/AogiriNetwork")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=Raiden,  buttons=BUTTON)
