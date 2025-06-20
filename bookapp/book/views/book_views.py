from flask import Blueprint, render_template, redirect, url_for, request
from book.models import Book
from book.forms import BookForm
from book import db

bp = Blueprint("book", __name__, url_prefix="/")


@bp.route("/list/")  # 여기 스타일은 끝에 '/'붙힘
def book_list():
    # ?page=2
    page = request.args.get("page", type=int, default=1)
    books = Book.query.order_by(Book.code.desc())
    books = books.paginate(page=page, per_page=10)
    return render_template("/book/list.html", books=books)


@bp.route("/details/<int:code>")
def book_details(code):
    book = Book.query.get_or_404(code)
    return render_template("/book/details.html", book=book)


@bp.route("/edit/<int:code>", methods=["GET", "POST"])
def book_edit(code):
    book = Book.query.get_or_404(code)

    if request.method == "POST":
        form = BookForm()

        if form.validate_on_submit():

            form.populate_obj(book)
            db.session.commit()

            return redirect(url_for("book.book_details", code=code))
        else:
            print("XXXXX")

    else:
        form = BookForm(obj=book)

    return render_template("/book/edit.html", form=form)


@bp.route("/delete/<int:code>")
def book_delete(code):
    book = Book.session.get(book, code)
    if book:
        db.session.delete(book)
        db.commit()
    return render_template("/book/list.html", book=book)


@bp.route("/create/", methods=["GET", "POST"])
def book_create():

    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            book = Book(
                title=form.title.data,
                author="길똥이",
                price=form.price.data,
                description=form.description.data,
            )
            db.session.add(book)
            db.session.commit()

            return redirect(url_for("book.book_list"))
        else:
            print("hi")

    else:
        return render_template("/book/create.html")
