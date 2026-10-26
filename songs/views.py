from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from songs.serializers import MusicSerializer
from films.models import movie

# Create your views here.


class MusicCreateView(CreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAdminUser]


    def post(self,request,pk=None):

        movie_id =pk

        movie_object =movie.objects.get(id=movie_id)

        form_data = request.data

        serializer_inst = MusicSerializer(data=form_data)

        if serializer_inst.is_valid():

            serializer_inst.save(movie=movie_object,created_by=request.user)

            return Response (data=serializer_inst.data)

        else:

            return Response (data=serializer_inst.errors)


# class MusicsRetrieveUpdateDeleteView()