from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from .models import Book
from .forms import BookCreate
from django.contrib import messages

from django.http import HttpResponse


# read
def index(request):
    results = Book.objects.all()
    return render(request, 'library.html', {'Book': results})


# show
def update_book(request, id):
    displayname = Book.objects.get(id=id)
    return render(request, "Upload_form.html", {'Book': displayname})


# update
def updatebook(request, id):
    update = Book.objects.get(id=id)
    form = BookCreate(request.POST, instance=update)
    if form.is_valid():
        form.save()
        messages.success(request, "successfully..!")
        return render(request, "Upload_form.html", {'Book': update})


# create
def create(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('author') and request.POST.get('email'):
            saverecord = Book()
            saverecord.name = request.POST.get('name')
            saverecord.author = request.POST.get('author')
            saverecord.email = request.POST.get('email')
            saverecord.save()
            messages.success(request, "Record save successful")
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def delete_book(request, id):
    delbook = Book.objects.get(id=id)
    delbook.delete()
    results = Book.objects.all()
    messages.success(request, 'Delete record successfull..')
    return render(request, 'library.html', {'Book': results})



