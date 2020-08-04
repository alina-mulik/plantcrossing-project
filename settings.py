import os

PORT = int(os.getenv("PORT", 8000))
print(PORT)

CACHE_AGE = 60 * 60 * 24

STATIC_URL = '/static/', '/font-awesome/', '/pict/'

STATICFILES_DIRS = [
    "static/style.css",
    "static/login.css",
    "pict/olive.jpg",
    "pict/favicon.ico",
    "pict/cactus.jpg",
    "font-awesome/css/font-awesome.css",
    "font-awesome.min.css",
]
