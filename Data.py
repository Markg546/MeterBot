from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}
Vă folosiți de {}

Pot extrage datele de pe contoare!
"""

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="Înapoi 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("Date contor", callback_data="date")
            InlineKeyboardButton("Cum se folosește?", callback_data="help"),
            InlineKeyboardButton("Despre", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
Vin în ajutor!

Apasați butonul "Date contor" sau trimiteți o poza și vă extrag datele!
    """

    # About Message
    ABOUT = """
**Despre**

Source Code : [Click aici](https://github.com/Markg546/MeterBot)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
AI : [Tesseract](https://github.com/tesseract-ocr/tesseract)
Cloud : [Heroku](www.heroku.com)

Developer : @markg546 și @MaxonSaxofon
    """
