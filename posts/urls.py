from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:pk>', PostDetailView.as_view()),
    path('', PostListView.as_view())
]