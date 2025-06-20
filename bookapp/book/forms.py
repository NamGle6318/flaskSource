from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class BookForm(FlaskForm):
    code = IntegerField()  # 책 코드번호
    title = StringField(validators=[DataRequired("title 필수 입력")])  # 책 이름
    price = IntegerField(validators=[DataRequired("price 필수 입력")])
    description = TextAreaField()  # 설명


class UserForm(FlaskForm):
    username = StringField(
        validators=[
            "아이디",
            DataRequired("아이디 필수 입력"),
            Length(min=3, max=20, message="아이디는 3~20 자리 사이여야합니다."),
        ]
    )
    password1 = StringField(
        validators=[
            "비밀번호",
            DataRequired("비밀번호 필수 입력"),
            EqualTo("password2", "비밀번호가 일치하지 않습니다."),
        ]
    )
    password2 = StringField(
        validators=["비밀번호 확인", DataRequired("비밀번호 필수 입력")]
    )
    email = EmailField(
        validators=[
            "이메일",
            DataRequired("이미 가입된 이메일"),
            Email("이메일 형식 확인"),
        ]
    )
