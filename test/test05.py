"""
    Created by RajZhao on 2018/11/08
"""

from werkzeug.local import LocalStack

s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)
s.push(1)
s.push(2)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)


