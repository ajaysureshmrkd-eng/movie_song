
from django.urls import path

from films.views import MovieListView,MovieCreateView,MovieRetrieveUpdateDeleteView

urlpatterns = [
    path("all/",MovieListView.as_view()),
    path("add/",MovieCreateView.as_view()),
    path("movies/<int:pk>/",MovieRetrieveUpdateDeleteView.as_view()),
]