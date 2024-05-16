from django.shortcuts import render

# ModelViewSet : 파일 및 이미지 업로드를 처리할 수 있는 API 구현

from rest_framework import viewsets
from .models import Document, Image
from .serializers import DocumentSerializer, ImageSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer