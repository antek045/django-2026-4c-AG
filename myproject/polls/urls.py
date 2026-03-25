from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('list_of_question.html', views.list_of_question, name='list'),
    path('login/', views.login_register_view, name='login'), 
]
