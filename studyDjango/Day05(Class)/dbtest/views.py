from django.shortcuts import render
from .models import Teacher

# Create your views here.
def index(request):
    t = Teacher.objects.all()
    context = {
        'var1': a,
        'var2': b,
        # key - html에서의 변수 : value - 값
    }
    return render(request, "dbtest/index.html", context)
