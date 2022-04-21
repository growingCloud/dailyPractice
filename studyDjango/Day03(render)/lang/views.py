from django.shortcuts import render

# Create your views here.
def c(request):
    return render(request, 'lang/c.html')

def python(request):
    return render(request, 'lang/python.html')