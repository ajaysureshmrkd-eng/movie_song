from rest_framework import serializers

from films.models import movie
from music.models import song
from music.serializers import SongSerializer

class MovieSerializer(serializers.ModelSerializer):

    track_count =serializers.SerializerMethodField(read_only=True)

    track = serializers.SerializerMethodField(read_only=True)



    class Meta:

        model = movie

        fields ="__all__"

        read_only_fields = ["id","created_at","updated_at","created_by"]


    def get_track_count(self,obj):

        return song.objects.filter(movie=obj).count()

    def get_track(self,obj):

        track_obj =song.objects.filter(movie=obj)

        serializer_inst =SongSerializer(track_obj,many=True)

        return serializer_inst.data

        