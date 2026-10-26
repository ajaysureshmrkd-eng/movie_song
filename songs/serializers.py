from rest_framework import serializers

from songs.models import Musics




class MusicSerializer(serializers.ModelSerializer):

    class Meta:

        model =Musics

        fields = "__all__"

        read_only_fields = ["id","created_at","updated_at","created_by","movie"]