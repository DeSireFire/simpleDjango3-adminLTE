from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index.as_view()),
    re_path('index\d?.html', views.index.as_view()),
]
