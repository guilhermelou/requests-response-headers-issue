import flask


def create_app():
    app = flask.Flask(__name__)

    @app.route("/multi-key-headers")
    def multi_key_service(*args, **kwargs):
        resp = flask.Response("Service Response")
        resp.headers.add("Content-Type", "text/plain")
        resp.headers.add("set-cookie", "COOKIE_1=COOKIE_VALUE_1")
        resp.headers.add("set-cookie", "COOKIE_2=COOKIE_VALUE_2")
        return resp

    return app