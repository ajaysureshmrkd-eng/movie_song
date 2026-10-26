from django.urls import path

from songs.views import MusicCreateView

urlpatterns = [
    path("movie/<int:pk>/",MusicCreateView.as_view()),
]