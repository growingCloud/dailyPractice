from django.shortcuts import render, redirect
from .models import Board


# Create your views here.
def index(request):
    b = Board.objects.all()
    context = {
        "bset": b
    }
    return render(request, "board/index.html", context)

def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    context = {
        "b": b
    }
    return render(request, "board/detail.html", context)

def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    b.delete()
    return redirect("board:index")