"""
    Created by RajZhao on 2018/11/07
"""
__author__ = "RajZhao"

from app.libs.helper import is_isbn_or_key
from yushu_book import YuShuBook
# from fisher import app
from flask import jsonify, request
from . import web
from app.forms.book import SearchForm


@web.route("/book/search")
def search():
    """
        q:普通关键字 isbn
        page
        isbn
    :return:
    """
    # Request Response
    q = request.args["q"]
    page = request.args["page"]
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == "isbn":
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
    # return json.dumps(result),200,{"content-type":"application/json"}
