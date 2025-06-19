from flask import Blueprint, render_template, request, redirect, url_for
from todo.models import Todo
from todo.forms import TodoForm
from datetime import datetime
from todo import db


# 별칭 = todo, default url = /todo
bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("/list/")
def todo_list():
    todos = Todo.query.filter(Todo.completed == 0).order_by(Todo.id.desc())
    return render_template("todo/todo_list.html", todos=todos)


@bp.route("/done/list")
def todo_done_list():
    todos = Todo.query.filter(Todo.completed == 1).order_by(Todo.id.desc())
    return render_template("todo/todo_done_list.html", todos=todos)


@bp.route("/detail/<int:id>")
def todo_detail(id):
    todo = Todo.query.get_or_404(id)  # id로 검색해서 있으면 찾고 없으면 404 에러
    return render_template("todo/todo_detail.html", todo=todo)


@bp.route("/register/", methods=["GET", "POST"])
def todo_register():
    form = TodoForm()
    if request.method == "POST" and form.validate_on_submit():
        todo = Todo(
            title=form.title.data,
            description=form.description.data,
            important=form.important.data,
            created=datetime.now(),
        )

        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("todo.todo_done", id=id))

    return render_template("todo/todo_create.html", form=form)


@bp.route("/done/<int:id>")
def todo_done(id):
    todo = Todo.query.get_or_404(id)  # id로 검색해서 있으면 찾고 없으면 404 에러
    todo.completed = True
    db.session.commit()
    return redirect(url_for("todo.todo_detail", id=todo.id))


@bp.route("/edit/<int:id>", methods=["GET", "POST"])
def todo_edit(id):
    todo = Todo.query.get_or_404(id)  # id로 검색해서 있으면 찾고 없으면 404 에러
    if request.method == "POST":
        form = TodoForm()
        if form.validate_on_submit():
            form.populate_obj(todo)  # 알아서 원본과 넣은 변수를 비교함
            db.session().commit()

            return redirect(url_for("todo.todo_detail", id=id))
    else:
        form = TodoForm(obj=todo)

    return render_template("todo/todo_edit.html", form=form)
