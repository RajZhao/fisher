"""
    Created by RajZhao on 2018/11/07
"""
__author__ = "RajZhao"

from helper import is_isbn_or_key
from yushu_book import YuShuBook
# from fisher import app
from flask import jsonify
from . import web


@web.route("/book/search/<q>/<page>")
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
    return jsonify(result)
    # return json.dumps(result),200,{"content-type":"application/json"}
