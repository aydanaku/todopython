from django.shortcuts import render, HttpResponse
from .models import ToDo, BookShop

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This is page test3.")

def bookshop(request):
    books_list = BookShop.objects.all()
    # books_title = bookshop.objects.title()
    # books_author = bookshop.objects.author()
    # books_date = bookshop.objects.date()
    return render(request, "books.html", {"books_list": books_list})