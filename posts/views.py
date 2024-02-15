from django.shortcuts import get_object_or_404, render
from posts.serializers import PostSerializer
from .models import Post
from rest_framework import viewsets, status, generics, mixins
from rest_framework .response import Response
from rest_framework .request import Request
from rest_framework.decorators import APIView, api_view
from rest_framework.permissions import IsAuthenticated

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    @api_view(http_method_names=["GET", "POST"])
    def homepage(request: Request):
        if request.method == "POST":
            data = request.data 
            response = {"message" : "Hello World!", "data":data}
            return Response(data = response, status = status.HTTP_201_CREATED)
        response = {"message" : "Hello World!"}
        return Response(data = response, status=status.HTTP_200_OK)
class PostListCreateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
     a view for creating and listing posts
    """
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    
    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
   
    
            
    
class PostRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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