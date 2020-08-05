import os
import socketserver
from http.server import SimpleHTTPRequestHandler
import settings

PORT = int(os.getenv("PORT", 8000))
print(PORT)


class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        path = self.build_path()

        if path == "/":
            self.handle_root()
        elif path == "/hello/":
            self.handle_hello()
        else:
            self.handle_404()

    def handle_root(self):
        return super().do_GET()

    def handle_hello(self):
        content: str = f"""
                <!DOCTYPE HTML>
                <html>
                <head>
                <title>PlantCrossing</title>
                 <style type="text/css"> 
                </style>
                </head>
                <body>
                <h1><align = center>Website Creator Info</align></h1>
                <h2>Mulik Alina Yur'evna</h2>
                </body>
                <p>Age: 24 years old<br> Position: QA engineer at ITechArt Groupпш</p>
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
                <p><align = center><img src="./pict/cactus.jpg id ="cactus" width=45%></align></p>
                </body>
                </html>
                """
        self.respond(msg, code=404, content_type="text/html")

    def respond(self, message, code=200, content_type="text/html"):
        self.send_response(code)
        self.send_header("Content-type", content_type)
        self.send_header("Content-length", str(len(message)))
        self.send_header("Cache-control", f"max-age={settings.CACHE_AGE}")
        self.end_headers()
        self.wfile.write(message.encode())

    def build_path(self) -> str:
        result = self.path

        if result[-1] != "/":
            result = f"{result}/"

        return result


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("it works")
        httpd.serve_forever(poll_interval=1)
