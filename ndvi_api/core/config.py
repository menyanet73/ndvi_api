import os
from starlette.config import Config


config = Config('.env')

DATABASE_URL = config('EE_DATABASE_URL', cast=str, default='')

EE_SERVICE_ACCOUNT = config('EE_SERVICE_ACCOUNT', cast=str, default='')

PALETTE = [
    '#ffffcc',
    '#d9f0a3',
    '#addd8e',
    '#78c679',
    '#41ab5d',
    '#238443',
    '#005a32'
    ]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath((__file__))))

PRIVATEKEY = os.path.join(BASE_DIR, 'privatekey.json')

MEDIA_DIR = os.path.join(BASE_DIR, 'media')
