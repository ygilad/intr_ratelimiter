from flask import Flask
from ratelimiter import RateLimiter


app = Flask(__name__)
server_limiter = None


@app.route('/')
def hello_world():
    return {'RateLimiter': server_limiter.get_params()}


def start(threshold, ttl):
    server_limiter = RateLimiter(threshold, ttl)
    app.run(port=80)

