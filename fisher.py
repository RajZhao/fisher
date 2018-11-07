import json

from flask import Flask, make_response
from helper import is_isbn_or_key
from yushu_book import YuShuBook

__author__ = "RajZhao"

app = Flask(__name__)
app.config.from_object("config")


@app.route("/book/search/<q>/<page>")
def search(q, page):
    """
        q:普通关键字 isbn
        page
        isbn
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == "isbn":
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return json.dumps(result),200,{"content-type":"application/json"}



def helloo():
    return "Hello, RajZhao"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=app.config["DEBUG"], port=81)