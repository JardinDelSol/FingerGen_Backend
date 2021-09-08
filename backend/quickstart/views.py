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
            out_dir = self.base_dir + "/modified.jpg"

            # run(img_dir, out_dir)

            # img64 = convert2base64(out_dir)

            # print(img64)

            # return Response(img64)

            # f = open(out_dir, "rb")
            # byte_im = f.read()

            f = open(img_dir, "rb")
            byte_im = f.read()

            print(byte_im[10])
            print(byte_im[11:20])

            # return Response(data=str(byte_im))
            return HttpResponse(byte_im, content_type="application/octet-stream")

            # return Response(img64, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
