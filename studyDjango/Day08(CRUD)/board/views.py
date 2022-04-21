from django.shortcuts import render, redirect
from .models import Board, Reply


# Create your views here.
def index(request):
    b = Board.objects.all()
    context = {
        "bset": b,
    }
    return render(request, "board/index.html", context)


def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()
    context = {
        "b": b,
        "rset": r,
    }
    return render(request, "board/detail.html", context)


def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    b.delete()
    return redirect("index")


def test(request):
    print(request.method)
    print(request.POST)
    return render(request, "board/test.html")

def create(request):
    if request.method == "POST":
        s = request.POST.get("subject")
        w = request.POST.get("writer")
        c = request.POST.get("content")
        Board(subject=s, writer=w, content=c).save()
        return redirect("index")
    return render(request, "board/create.html")

def update(request, bpk):
    b = Board.objects.get(id=bpk)
    if request.method == "POST":
        s = request.POST.get("subject")
        w = request.POST.get("writer")
        c = request.POST.get("content")
        b.subject, b.writer, b.content = s, w, c
        b.save()
        return redirect("detail", bpk)
    context = {
        "b" : b
    }
    return render(request, "board/update.html", context)

def creply(request, bpk):
    b = Board.objects.get(id=bpk)
    r = request.POST.get("rep")
    c = request.POST.get("com")
    Reply(board=b, replyer=r, comment=c).save()
    return redirect("detail", bpk)

def dreply(request, bpk, rpk):
    r = Reply.objects.get(id=rpk)
    r.delete()
    return redirect("detail", bpk)