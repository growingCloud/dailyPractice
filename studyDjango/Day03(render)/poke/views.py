from django.shortcuts import render

# Create your views here.
def pika(request):
    return render(request, 'poke/pika.html')
