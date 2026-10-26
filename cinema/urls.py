from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken
from cinema.views import AdminView
from cinema.views import UserView


urlpatterns = [
    path("admin/",AdminView.as_view()),
    path("user/",UserView.as_view()),

    path("token/",ObtainAuthToken.as_view()),

]
