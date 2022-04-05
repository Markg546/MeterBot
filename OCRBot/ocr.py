import os
import pytesseract
from PIL import Image
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.errors import MessageEmpty

# pytesseract.pytesseract.tesseract_cmd = r""


@Client.on_message(filters.private & filters.incoming & filters.photo)
async def _ocr(_, msg: Message):
    user_id = msg.from_user.id
    message_id = msg.message_id
    name_format = f"Photo_{user_id}_{message_id}"
    message = await msg.reply("Asteptati...")
    image = await msg.download(file_name=f"{name_format}.jpg")
    img = Image.open(image)
    text = pytesseract.image_to_string(img, config='outputbase digits')
    text = text[:-1]
    try:
        await msg.reply(text, quote=True, disable_web_page_preview=True)
    except MessageEmpty:
        await msg.reply("Nu inteleg textul...", quote=True)
    await message.delete()
    os.remove(image)
