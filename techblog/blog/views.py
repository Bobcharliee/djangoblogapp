
from rest_framework import generics
from .models import blog
from .permissions import IsAuthorOrReadOnly
from .serializers import blogserializer

class Bloglist(generics.ListCreateAPIView):
    queryset = blog.objects.all()
    serializer_class = blogserializer


class Blogdetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = blog.objects.all()
    serializer_class = blogserializer