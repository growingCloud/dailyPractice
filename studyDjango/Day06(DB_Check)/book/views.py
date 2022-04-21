from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    b = Book.objects.all()
    context = {
        "bset" : b
    }
    return render(request, "book/index.html", context)
