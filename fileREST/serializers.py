from rest_framework import serializers
from .models import Document, Image

# 파일과 이미지를 업로드하고 처리 by ModelSerializer

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'description', 'document', 'uploaded_at']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'title', 'image', 'uploaded_at']
