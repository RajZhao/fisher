"""
    Created by RajZhao on 2018/11/07
"""

from wtforms.validators import Length, NumberRange, DataRequired
from wtforms import Form, StringField, IntegerField


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)



