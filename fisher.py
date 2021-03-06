import json

from flask import Flask

from app import create_app

__author__ = "RajZhao"

app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=81, threaded=True)
