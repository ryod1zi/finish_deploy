from django.urls import path
from .views import *


urlpatterns = [
    path('create/', CarCreateView.as_view()),
    path('', CarListView.as_view()),
    path('<int:pk>/', CarDetailView.as_view())
]

