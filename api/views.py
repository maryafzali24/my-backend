
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post


# Endpoint 1: List all posts and create a new post
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Endpoint 2: Retrieve, update, or delete a specific post
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer