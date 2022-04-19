from rest_framework import generics
from rest_framework import viewsets
from .models import Post
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer