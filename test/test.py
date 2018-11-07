"""
    Created by RajZhao on 2018/11/07
"""

from flask import Flask, current_app

app = Flask(__name__)
# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config["DEBUG"]
# ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.config["DEBUG"]


# 实现上下文协议的对象使用with
# 上下文管理器
# __enter__ __exit__

# try:
#     f = open(r"D:\t.txt")
#     print(f.read())
# finally:
#     f.close()
#
# with open(r"") as f:
#     print(f.read())

# class A:
#     def __enter__(self):
#         a = 1
#         return a
#
#     def __exit__(self):
#         a = 2
#         return a
#
# with A() as obj_A:
#     pass


class MyResource:
    def __enter__(self):
        print("connect to resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print("process exception")
        else:
            print("no exception")
        print("close resource connection")
        return True

    def query(self):
        print("query data")

with MyResource() as resource:
    resource.query()
