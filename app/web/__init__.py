"""
    Created by RajZhao on 2018/11/07
"""
__author__ = "RajZhao"

from flask import Blueprint

web = Blueprint("web", __name__)

from app.web import book
from app.web import user
