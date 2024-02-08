from django.shortcuts import render
from .serializers import SignUPSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.

class SignUPView(generics.GenericAPIView):
    serializer_class = SignUPSerializer

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data = data) 
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User created successful",
                "data": serializer.data,
            }
            return Response(data = response, status= status.HTTP_201_CREATED)
        # if any errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

