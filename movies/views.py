from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieModel
from .permissions import IsOwnOrReadOnly
from common.pagination import CustomPagination


class MovieViewSet(viewsets.ModelViewSet):
    """
        This class used to display movie information
    """
    serializer_class = MovieSerializer
    queryset = MovieModel.objects.all()
    permission_classes = [IsOwnOrReadOnly]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        # Assign the user who created the movie
        serializer.save(creator=self.request.user)

