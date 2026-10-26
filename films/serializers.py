from rest_framework import serializers

from films.models import movie


class MovieSerializer(serializers.ModelSerializer):


    class Meta:

        model = movie

        fields ="__all__"

        read_only_fields = ["id","created_at","updated_at","created_by"]

        