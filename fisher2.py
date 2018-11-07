from flask import Flask, make_response

__author__ = "RajZhao"

app = Flask(__name__)
app.config.from_object("config")


@app.route("/hello")
def hello():
    headers = {
        "content-type": "application/json",
        "location": "http://www.baidu.com"
    }
    # response = make_response("<html></html>", 301)
    # response.headers = headers
    # return "Hello, RajZhao"
    return "<html></html>", 301, headers
    # return response


def helloo():
    return "Hello, RajZhao"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=81)
