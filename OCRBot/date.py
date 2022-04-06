from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Help Message
@Client.on_message(filters.private & filters.incoming & filters.command("date"))
async def _help(bot, msg):
    await bot.send_photo(
        msg.chat.id,
        "https://i.imgur.com/WGbwhqH.jpg",
        caption="00637",
        #reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )
    await message.delete()

