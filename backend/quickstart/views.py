from django.shortcuts import render
from .serializer import ImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.http import HttpResponse
import base64
import cv2
import numpy as np
import os
import json
import sys
from .process import run
import time

# Create your views here.

sys.path.append(os.getcwd())


def convert2base64(img_dir):
    with open(img_dir, "rb") as image_file:
        base64str = base64.b64encode(image_file.read())
        return base64str


class FakeFingerprintAPIView(APIView):
    def __init__(self):
        self.base_dir = os.getcwd()

    def post(self, request):
        # print(request.data)
        file_serializer = ImageSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            img_dir = file_serializer.data["file"]

            img_dir = self.base_dir + img_dir
            out_dir = self.base_dir + "/media/modified.jpg"

            # run(img_dir, out_dir)
            time.sleep(20)

            img64 = convert2base64(out_dir)

            return HttpResponse(content=img64)

        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
