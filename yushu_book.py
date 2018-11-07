"""
    Created by RajZhao on 2018/11/06
"""
__author__ = "RajZhao"

from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    per_page = 15
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = YuShuBook.isbn_url.format(isbn)
        print("url", url)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = YuShuBook.keyword_url.format(keyword, current_app.config["PER_PAGE"], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config["PER_PAGE"]
