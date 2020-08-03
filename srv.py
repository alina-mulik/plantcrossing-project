import os
import socketserver
from http.server import SimpleHTTPRequestHandler

PORT = int(os.getenv("PORT", 8000))
print(PORT)

class MyHandler(SimpleHTTPRequestHandler):

    def main_headers_html(self):
        self.send_headers("Content-type", "text/html")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Content-length", str(len()))

    def handle_root(self):
        self.send_response(404)
        root = open("index.html", 'r')
        self.send_response(404)
        self.main_headers(root)
        self.wfile.write(root.encode())

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
        self.main_headers(content)
        self.wfile.write(content.encode())

    def handle_404(self):
        self.send_response(404)
        msg = f"""
                <!DOCTYPE HTML>
                <html>
                <head>
                <title>PlantCrossing</title>
                <style type="text/css"> 
                </style>
                </head>
                <body>
                <h1><align = center> Ooops, something went wrong. Perhaps, you meant <a href = "https://plantcrossing.herokuapp.com/">plantcrossing.herokuapp.com</a>?</align></h1>
                <p><align = center><img src="./pict/cactus.jpgid ="cactus" width=45%></align></p>
                </body>
                </html>
                """
        self.send_response(404)
        self.main_headers(msg)
        self.wfile.write(msg.encode())

    def respond(self, code):
        pass

    def built_path(self):
        path = self.built_path()
        result = self.path
        if self.path[-1] != "/":
            result = f"{result}/"
        else:
            pass

    def do_GET(self):
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
