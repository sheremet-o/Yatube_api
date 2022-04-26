from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, filters

from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination


from .serializers import GroupSerializer, PostSerializer, CommentSerializer
from .serializers import FollowSerializer
from posts.models import Group, Post, Comment, Follow

User = get_user_model()


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = IsOwnerOrReadOnly,
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = IsOwnerOrReadOnly,


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = IsOwnerOrReadOnly,

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = IsAuthenticated,
    filter_backends = filters.SearchFilter,
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
