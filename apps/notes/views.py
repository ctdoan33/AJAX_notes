# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    context = {
        "notes" : Note.objects.all(),
    }
    return render(request, "notes/index.html", context)
def create(request):
    if request.method == "POST":
        Note.objects.create(title=request.POST["title"])
        context = {
            "notes" : Note.objects.all(),
        }
        return render(request, "notes/notes.html", context)
def delete(request, id):
    if request.method == "POST":
        Note.objects.get(id=int(id)).delete()
        context = {
            "notes" : Note.objects.all(),
        }
        return render(request, "notes/notes.html", context)
def update(request, id):
    if request.method == "POST":
        update = Note.objects.filter(id=int(id)).update(description=request.POST["description"])
    return HttpResponse("updated description "+id)