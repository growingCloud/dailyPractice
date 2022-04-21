from django.urls import path
from lang import views  # from. import views (같은 폴더는 .으로 표현 가능)

urlpatterns = [
    path('c/', views.c),
    path('python/', views.python)
]