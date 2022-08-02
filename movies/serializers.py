from rest_framework import serializers
from .models import MovieModel


class MovieSerializer(serializers.ModelSerializer):
    """
        This class used to serialize input data
    """

    class Meta:
        model = MovieModel
        fields = ['id', 'title', 'genre', 'creator', 'year']
        # extra_kwargs = {
        #     'creator': {'read_only': True}
        # }