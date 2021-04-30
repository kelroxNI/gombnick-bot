import sys
import time
import telepot
from PIL import Image, ImageFilter
from telepot.loop import MessageLoop
from forismatic import *
import random

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'photo':
        bot.download_file(msg['photo'][-1]['file_id'], './file.png')
        im = Image.open("file.png").convert("P")
        palettedata = []
        for i in range(12):
            r = random.randint(0,255)
            palettedata.append(r)
        im.putpalette(palettedata)
        im.save("edited.png")
        f = forismatic.ForismaticPy()
        z = f.get_Quote('ru')
        bot.sendPhoto(chat_id, photo=open('./edited.png', 'rb'), caption=z[0])

bot = telepot.Bot('*YOUR TOKEN HERE')
MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
