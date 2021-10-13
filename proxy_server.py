import os

import requests
import flask
from dotenv import load_dotenv

load_dotenv()

THIRD_PARTY_URL = os.environ.get("THIRD_PARTY_URL")


def create_app():
    app = flask.Flask(__name__)

    @app.route("/proper-multi-key-header-handling")
    def proper_multi_key(*args, **kwargs):
        response = requests.get(f"{THIRD_PARTY_URL}/multi-key-headers")
        new_resp = flask.Response("Proxy Response")

        # Handling directly from urllib3 instead of using requests
        # merged dict
        for key, value in response.raw.headers.iteritems():
            new_resp.headers.add(key, value)

        new_resp.headers.remove("Content-Length")
        return new_resp

    @app.route("/wrong-multi-key-header-handling")
    def wrong_multi_key(*args, **kwargs):
        response = requests.get(f"{THIRD_PARTY_URL}/multi-key-headers")
        new_resp = flask.Response("Proxy Response")

        for key, value in response.headers.items():
            new_resp.headers.add(key, value)

        new_resp.headers.remove("Content-Length")
        return new_resp


    return app
