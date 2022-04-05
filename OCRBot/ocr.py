import os
import pytesseract
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import MessageEmpty
import cv2
import numpy as np

# pytesseract.pytesseract.tesseract_cmd = r""

@Client.on_message(filters.private & filters.incoming & filters.photo)
async def _ocr(_, msg: Message):
    user_id = msg.from_user.id
    message_id = msg.message_id
    name_format = f"Photo_{user_id}_{message_id}"
    message = await msg.reply("Asteptati...")
    image = await msg.download(file_name=f"{name_format}.jpg")
    img = np.asarray(Image.open(image))
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # pre-processing starts here
    img = cv2.fastNlMeansDenoising(img, None, 10, 7, 21)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    img = cv2.erode(img, np.ones((3,2),np.uint8), iterations = 1)
    
    text = pytesseract.image_to_string(img, lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
    
    text = text[:-1]
    try:
        await msg.reply(text, quote=True, disable_web_page_preview=True)
    except MessageEmpty:
        await msg.reply("Nu inteleg textul...", quote=True)
    await message.delete()
    os.remove(image)
