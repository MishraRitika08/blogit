from django.db.migrations import serializer
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



'''
ModelViewSet already provides methods for:
Method	Purpose
list() ->	Fetch all posts
retrieve() ->	Fetch one post
create() ->	Create a post
update() ->	Fully update a post
partial_update() ->	Partially update a post
destroy() ->	Delete a post

You don't need to implement these methods yourself for basic CRUD.'''