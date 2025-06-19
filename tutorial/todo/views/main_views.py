from flask import Blueprint, redirect, url_for

# bp = Blueprint("별칭", 실행되는 모듈명 가져오기, url_prefix="/")
bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/")
def index():
    return redirect(url_for("todo.todo_list"))  # bluePrint로 등록한 별칭을 통해 접근
