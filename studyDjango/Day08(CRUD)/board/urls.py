from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("detail/<bpk>", views.detail, name="detail"),
    path("delete/<bpk>", views.delete, name="delete"),
    path('test/', views.test),
    path("create/", views.create, name="create"),
    path("update/<bpk>", views.update, name="update"),
    path("creply/<bpk>", views.creply, name="creply"),
    path("dreply/<bpk>/<rpk>", views.dreply, name="dreply"),
]
