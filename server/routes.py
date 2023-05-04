from flask import send_from_directory
from server import app


@app.route("/", defaults={"path": "index.html"})
@app.route("/<path:path>")
def catch_all(path):
    return send_from_directory("../client/dist", path)


@app.route("/api/test")
def test():
    return "Hello Flask!"
