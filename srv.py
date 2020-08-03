import os
import socketserver
from http.server import SimpleHTTPRequestHandler

PORT = int(os.getenv("PORT", 8000))
print(PORT)

cc = "Cache-control"
nc = "Cache-Control:no-cache, no-store"
pubc = "Cache-Control:public, max-age=600"
privc = "Cache-Control:private, max-age=600"

ct = "Content-type"
plain = "text/plain"
html = "text/html"
gif = "image/gif"
jpeg = "image/jpeg"

class MyHandler(SimpleHTTPRequestHandler):
    def content_header(self):
        ct = "Content-type"
        plain = "text/plain"
        html = "text/html"
        gif = "image/gif"
        jpeg = "image/jpeg"
        self.send_header()

    def cache_control(self):
        cc = "Cache-control"
        nc = "Cache-Control:no-cache, no-store"
        pubc = "Cache-Control:public, max-age=600"
        privc = "Cache-Control:private, max-age=600"
        self.send_headers()

    def main_headers(self):
        self.send_header("Content-length", str(len()))
        self.wfile.write(().encode())

    def handle_root(self):
        self.send_response(404)
        root = ("index.html")
        self.send_response(404)
        self.content_header(ct, html)
        self.cache_control(cc, privc)
        self.main_headers(root)

    def handle_hello(self):
        content = f"""
                <!DOCTYPE HTML>
                <html>
                <head>
                <title>PlantCrossing</title>
                 <style type="text/css"> 
                </style>
                </head>
                <body>
                <h1><align = center>Webcite Creator Info</align></h1>
                <h2>Mulik Alina Yur'evna</h2>
                </body>
                <p>PATH: {self.path} </p>
                </html>
                """
        self.send_response(200)
        self.content_header(ct, html)
        self.cache_control(cc, privc)
        self.main_headers(content)

    def handle_404(self):
        self.send_response(404)
        msg = f"""
                <!DOCTYPE HTML>
                <html>
                <head>
                <title>PlantCrossing</title>
                <style type="text/css"> 
                #cactus {
                    width: 40%;
                }
                </style>
                </head>
                <body>
                <h1><align = center> Ooops, something went wrong. Perhaps, you meant <a href = "https://plantcrossing.herokuapp.com/">plantcrossing.herokuapp.com</a>?</align></h1>
                <p><align = center><img id ="cactus" src="./pict/cactus.jpg></align></p>
                </body>
                </html>
                """
        self.send_response(404)
        self.content_header(ct, html)
        self.cache_control(cc, privc)
        self.main_headers(msg)

    def respond(self, code):
        pass

    def built_path(self):
        result = self.path
        if self.path[-1] != "/":
            result = f"{result}/"
        else:
            pass

    def do_GET(self):
        path = self.build_path()
        if self.path == "/":
            self.handle_root()
        elif self.path == "/hello/":
            self.handle_hello()
        else:
            self.handle_404()


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("it" + " works")
        httpd.serve_forever(poll_interval=1)
