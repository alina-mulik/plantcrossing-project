import traceback
from datetime import datetime
from http.server import SimpleHTTPRequestHandler
import settings
from custom_types import Url
from errors import NotFound
from utils import get_content_type
from utils import get_user_data
from utils import read_static
from utils import to_bytes


class MyHttp(SimpleHTTPRequestHandler):
    def do_GET(self):
        url = Url.from_path(self.path)
        content_type = get_content_type(url.file_name)
        endpoints = {
            "/": [self.handle_root, []],
            "/hello/": [self.handle_hello, [url]],
            "/style/": [self.handle_static, [f"style/{url.file_name}", content_type]],
            "/pict/": [self.handle_static, [f"pict/{url.file_name}", content_type]],
            "/css/": [self.handle_icons, [f"css/{url.file_name}", content_type]],
        }
        try:
            handler, args = endpoints[url.normal]
            handler(*args)
        except (KeyError, NotFound):
            self.handle_404()
        except Exception:
            self.handle_500()

    def handle_static(self, file_path, ct):
        content = read_static(file_path)
        self.respond(content, content_type=ct)

    def handle_root(self):
        return super().do_GET()

    def handle_500(self):
        self.respond(traceback.format_exc(), code=500, content_type="text/plain")

    def handle_icons(self):
        icons_file = settings.STATIC_DIR / "font-awesome" / "css" / "font-awesome.min.css"
        with icons_file.open("r") as fp:
            icons = fp.read()

        self.respond(icons, content_type="text/css")

    def handle_hello(self, url):
        user = get_user_data(url.query_string)
        year = datetime.now().year - user.age

        content = f"""
        <html>
        <head><title>Study Project Z33 :: Hello</title></head>
        <body>
        <h1>Hello {user.name}!</h1>
        <h1>You was born at {year}!</h1>
        <p>path: {self.path}</p>

        <form>
            <label for="name-id">Your name:</label>
            <input type="text" name="name" id="name-id">
            <label for="age-id">Your age:</label>
            <input type="text" name="age" id="age-id">
            <button type="submit" id="greet-button-id">Greet</button>
        </form>

        </body>
        </html>
        """

        self.respond(content)

    def handle_404(self):
        msg = f"""
                    <!DOCTYPE HTML>
                    <html>
                    <head>
                    <title>PlantCrossing</title>
                    <style type="text/css"> 
                    </style>
                    </head>
                    <body>
                    <h1><align = center> Ooops, something went wrong. Perhaps, you meant 
    <a href = "https://plantcrossing.herokuapp.com/">plantcrossing.herokuapp.com</a>?</align></h1> 
                    <p><align = center><img src="/static/pict/cactus.jpg" id ="cactus" width=45%></align></p>
                    </body>
                    </html>
                    """
        self.respond(msg, code=404, content_type="text/html")

    def respond(self, message, code=200, content_type="text/html"):
        payload = to_bytes(message)

        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.send_header("Content-length", str(len(payload)))
        self.send_header("Cache-control", f"max-age={settings.CACHE_AGE}")
        self.end_headers()
        self.wfile.write(payload)


