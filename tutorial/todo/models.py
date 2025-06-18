# entity

from todo import db
from sqlalchemy import text


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    created = db.Column(db.DateTime(), nullable=False)
    completed = db.Column(db.Boolean(), default=False, server_default=text("false"))
    important = db.Column(db.Boolean(), default=False, server_default=text("false"))
