# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=225)
    year_of_birth = models.IntegerField(blank=True)

    class Meta:
        default_related_name = 'authors'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default="No set")
    book_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    release_date = models.DateField()
    category = models.CharField(max_length=100)

    class Meta:
        default_related_name = 'books'

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=225, blank=True)

    class Meta:
        default_related_name = 'clients'

    def __str__(self):
        return self.name


class Sale(models.Model):
    client = models.ForeignKey(Client)
    books = models.ManyToManyField(Book)
    time_of_sale = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        total = 0
        for b in self.books:
            total += b.price
        return total

    def __str__(self):
        return self.time_of_sale
