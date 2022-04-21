from django.urls import path
from lol import views

urlpatterns = [
    path('kennen/', views.kennen),
]