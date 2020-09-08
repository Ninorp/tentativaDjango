# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")


def books(request):
    bs = Book.objects.all()
    output = ', '.join([b.title for b in bs])
    return HttpResponse(output)