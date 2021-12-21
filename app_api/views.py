from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .serializers import CartItemSerializers
from .models import CartItem

# Create your views here.
class CartItemViews(APIView):
    def post(self, request):
        serializer = CartItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ({"status":"success", "data":serializer.data}, status=status.HTTP_200_ok)
        else:
            return Response({"status":"error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
