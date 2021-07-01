
from .models import Book, db
from flask import Blueprint, request, render_template, redirect, url_for
import sqlite3
views = Blueprint("views", __name__, static_folder="static",
                  template_folder="templates")


@views.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #
        is_read = None
        if request.form.get("read") == "False":
            is_read = False
        elif request.form.get("read") == "True":
            is_read = True

        # create a new book object
        new_book = Book(
            book_name=request.form["bname"],
            author=request.form["author"],
            theme=request.form["theme"],
            pub_year=request.form["year"],
            is_read=is_read
        )

        # add and commit to database the new book entry
        db.session.add(new_book)
        db.session.commit()

        # redirect to books page
        return redirect(url_for("views.get_books"))

    return render_template("index.html")


@views.route("/books")
def get_books():
    all_books = Book.query.order_by(Book.date_added).all()
    all = Book.query.all()
    return render_template("books.html", books=all_books,total = all)


@views.route("/tech")
def dis_tech():
    tech_books  = Book.query.filter_by(theme = 'technology').all()
    return render_template('technologies.html',books = tech_books)


@views.route("/books/delete/<id>")
def delete_book(id):
    book = Book.query.get_or_404(
        int(id), description=f"Cannot delete because cannot find a book with this id => {id}. Try with another id")
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("views.get_books"))


@views.route("/books/edit/<int:id>", methods=["GET", "POST"])
def edit_book(id):
    book = Book.query.get_or_404(
        int(id), description=f"CANNOT EDIT: the book whose id is {id}, can't be found. Try with another id")

    if request.method == "POST":
        book.book_name = request.form.get("bname")
        book.author = request.form.get("author")
        book.theme = request.form.get("theme")
        book.pub_year = request.form.get("year")

        if request.form.get("read") == "False":
            book.is_read = False
        elif request.form.get("read") == "True":
            book.is_read = True

        db.session.commit()
        return redirect(url_for("views.get_books"))
    else:
        return render_template("edit.html", book=book)
