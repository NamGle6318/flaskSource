# entity

from book import db
from sqlalchemy import text


class Book(db.Model):
    code = db.Column(db.Integer, primary_key=True)  # 책 코드번호
    title = db.Column(db.String(100), nullable=False)  # 책 이름
    author = db.Column(db.String(50), nullable=False)  # 작가
    description = db.Column(db.Text())  # 설명
    price = db.Column(db.Integer, nullable=False)


# 사용자 모델
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
