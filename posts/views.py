from django.shortcuts import get_object_or_404, render
from posts.serializers import PostSerializer
from .models import Post
from rest_framework import viewsets, status
from rest_framework .response import Response
from rest_framework .request import Request


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# # Create your views here.
# class PostViewset(viewsets.ViewSet):
#     def list (self, request:Request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(instance = queryset, many = True)
#         return Response(data = serializer.data, status = status.HTTP_200_OK)
    
#     def retrieve(self, request:Request, pk = None):
#         post = get_object_or_404(post, pk = pk)
#         serializer = PostSerializer(instance = post)
#         return Response(data = serializer.data, status= status.HTTP_200_OK)