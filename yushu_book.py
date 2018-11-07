"""
    Created by RajZhao on 2018/11/06
"""
__author__ = "RajZhao"

from httper import HTTP


class YuShuBook:
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = YuShuBook.isbn_url.format(isbn)
        print("url", url)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = YuShuBook.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result
