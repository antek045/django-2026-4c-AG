from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # Generic Class-Based Views
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    
    # Standard Function Views
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("list/", views.list_of_question, name="list"),
]
