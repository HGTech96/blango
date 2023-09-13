from rest_framework import generics
from rest_framework.authentication import SessionAuthentication

from blog.models import Post
<<<<<<< HEAD
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
=======
from blango_auth.models import User
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer
>>>>>>> e5a7c7f64a8db5e4d9987bb8711c1cd5d757a45a


class PostList(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
<<<<<<< HEAD
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
=======
    # permission_classes = [AuthorModifyOrReadOnly | IsAdminUser]
>>>>>>> e5a7c7f64a8db5e4d9987bb8711c1cd5d757a45a
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer