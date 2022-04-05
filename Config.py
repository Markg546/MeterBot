import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("API_ID nu e valid")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
else:
    # Fill the Values
    API_ID = 15837822
    API_HASH = "ce1fa5adff9380657b5906496cd27ec7"
    BOT_TOKEN = "5226475789:AAHD4jCUpw1oaQIlgsaMxSXn7NkVD8pt3As"
