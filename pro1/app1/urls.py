from django.urls import path
from .views import *
urlpatterns = [
    path("ev/",eview),
    path("sv/",sview),
    path("uv/<int:pk>/",uview),
    path("dv/<int:k>/",dview),
]