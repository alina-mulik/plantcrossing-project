import os

PORT = int(os.getenv("PORT", 8000))
print(PORT)

CACHE_AGE = 60 * 60 * 24

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    "static/style.css",
    "static/login.css",
    "static/pict/olive.jpg",
    "static/pict/favicon.ico",
    "static/pict/cactus.jpg",
    "static/font-awesome/css/font-awesome.min.css"

]
