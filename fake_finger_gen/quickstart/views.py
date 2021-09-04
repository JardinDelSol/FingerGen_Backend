from django.shortcuts import render
from .serializer import ImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
import base64
from Fake_Fingerprint_Generation

# Create your views here.


def convert2base64(img_dir):
    with open(img_dir, "rb") as image_file:
        base64str = base64.b64encode(image_file.read())
        return base64str


class FakeFingerprintAPIView(APIView):
    def post(self, request):
        file_serializer = ImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
