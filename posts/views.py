from rest_framework import generics
from rest_framework import viewsets
from .models import Post
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_context(self):
        lan_code = self.request.query_params.get("lan_code")
        return {"request": self.request, "lan_code": lan_code}



class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer