from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Book(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=20)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)