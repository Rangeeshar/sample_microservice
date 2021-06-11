import tornado.ioloop
from  tornado.web import RequestHandler
import requests
import json

JOKE_URL = "https://official-joke-api.appspot.com/jokes/programming/random"
VALIDATE_KEY = "http://localhost:8080/api/validate?api_key={}"

class MainHandler(RequestHandler):
    async def get(self):
        api_key = self.get_argument("api_key")
        validate_res = requests.get(VALIDATE_KEY.format(api_key), timeout=3)
        if validate_res.status_code == 200:
            validate_res = json.loads(validate_res.content)
            if not validate_res.get("success"):
                self.write({"success": False, "message":"not a valid api_key", "data": {}})
            else:
                res  = requests.get(JOKE_URL, timeout=2)
                if res.status_code == 200:
                    res = json.loads(res.content)
                    self.write({"success": True, "message": "found a random joke for you", "data": res})
                else:
                    self.write({"success": False, "message": "cant fetch joke, this is not a joke ", "data": {}})

def make_app():
    return tornado.web.Application([
        (r"/api/joke", MainHandler),
    ])

if __name__ == "__main__":
    try:
        app = make_app()
        app.listen(8081)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("shutting down server gracefully")
        tornado.ioloop.IOLoop.current().stop()