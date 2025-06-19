# entity
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired


# dto
class TodoForm(FlaskForm):
    title = StringField(validators=[DataRequired("제목 필수 입력")])
    description = TextAreaField(validators=[DataRequired("상세 필수 입력")])
    completed = BooleanField()
    important = BooleanField()
