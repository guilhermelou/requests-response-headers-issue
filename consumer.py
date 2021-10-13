import os

import requests
import flask
from dotenv import load_dotenv

load_dotenv()

PROXY_URL = os.environ.get("PROXY_URL")


def validate_headers(response):
    assert len(response.raw.headers.getlist('set-cookie')) == 2, (
        "We are expecting 2 set-cookie headers")


def create_app():
    app = flask.Flask(__name__)

    @app.route("/proper-handling")
    def proper_handling(*args, **kwargs):
        response = requests.get(f"{PROXY_URL}/proper-multi-key-header-handling")
        validate_headers(response)
        return {}

    @app.route("/wrong-handling")
    def wrong_handling(*args, **kwargs):
        response = requests.get(f"{PROXY_URL}/wrong-multi-key-header-handling")
        validate_headers(response)
        return {}

    return app
