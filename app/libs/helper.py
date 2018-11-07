"""
    Created by RajZhao on 2018/11/06
"""
__author__ = "RajZhao"

def is_isbn_or_key(word):
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"
    short_q = word.replace("-", "")
    if "-" in word and len(short_q) == 10 and word.replace(short_q).isdigit:
        isbn_or_key = "isbn"
    return isbn_or_key
