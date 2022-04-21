from django.urls import path
from poke import views

urlpatterns = [
    path('pika/', views.pika),
]