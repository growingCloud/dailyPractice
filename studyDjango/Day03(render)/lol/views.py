from django.shortcuts import render

# Create your views here.
def kennen(request):
    return render(request, 'lol/kennen.html')
