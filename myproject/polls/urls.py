from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_of_question.html', views.list_of_question, name='list'),
]
