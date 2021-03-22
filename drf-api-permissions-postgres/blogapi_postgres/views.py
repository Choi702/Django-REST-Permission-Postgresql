from blogapi_postgres.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import blogapi_postgres
from .serializers import blogapi_postgresSerializer


class blogapi_postgresList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = blogapi_postgres.objects.all()
    serializer_class = blogapi_postgresSerializer

class blogapi_postgresDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = blogapi_postgres.objects.all()
    serializer_class = blogapi_postgresSerializer
