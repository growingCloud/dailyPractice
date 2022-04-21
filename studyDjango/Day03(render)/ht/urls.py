from django.urls import path
from ht import views

urlpatterns = [
    path('block/', views.block),
    path('inline/', views.inline)
]