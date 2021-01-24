from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def add_todo(request):
    form = request.POST
    # print(form)
    text = form["todo_text"]
    # print(text)
    todo = ToDo(text=text)
    todo.save()
    # return HttpResponse("Форма получена")
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)

def third(request):
    return HttpResponse("This is page test3.")

def book(request):
    book_list = Book.objects.all()
    return render(request, "books.html", {"book_list": book_list})

def delete_book(request, id):
    book_list = Book.objects.get(id=id)
    book_list.delete()
    return redirect(book)

def mark_book(request, id):
    book_list = Book.objects.get(id=id)
    book_list.is_favorite = not book_list.is_favorite
    book_list.save()
    return redirect(book)

def close_book(request, id):
    book_list = Book.objects.get(id=id)
    book_list.is_closed = not book_list.is_closed
    book_list.save()
    return redirect(book)

def add_book(request):
    form = request.POST
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    book_list = Book(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book_list.save()
    # return HttpResponse("Форма получена")
    return redirect(book)