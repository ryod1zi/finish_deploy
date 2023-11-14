from rest_framework.decorators import action
from rest_framework import permissions
from .models import Car
from .serializers import *
from .permissions import IsAuthorOrAdmin
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class Pagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'page'


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title', )
    filterset_fields = ('category', 'year')


class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CarListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarListSerializer
        return CarSerializer


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.request.method in ('PUT', 'PATCH'):
            return CarCreateView
        return CarSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return IsAuthorOrAdmin(),
        elif self.request.method in ('PUT', 'PATCH'):
            return IsAuthorOrAdmin(),
        return permissions.AllowAny(),

