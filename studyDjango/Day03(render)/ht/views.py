from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def block(request):
    return render(request, "ht/block.html")

def inline(request):
    return render(request, "ht/inline.html")