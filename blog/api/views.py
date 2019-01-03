from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from blog.models import Post
from .serializers import (PostAllSerializer, PostCreateSerializer, PostUpdateSerializer)
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny)
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import (SearchFilter, OrderingFilter)
from .pagination import (PostLimitOffsetPagination, PostPageNumberPagination)

class AddPostAPI(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostsAPIList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostAllSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__first_name']
    pagination_class = PostLimitOffsetPagination

class SinglePostAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostAllSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EditePostAPI(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        post.delete()

class DeletePostAPI(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostAllSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'id'
