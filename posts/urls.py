from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('<int:pk>', PostDetailView.as_view()),
    path('', PostListView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls