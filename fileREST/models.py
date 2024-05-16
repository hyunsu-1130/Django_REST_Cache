from django.db import models

# ImageField 또는 FileField를 사용하여 해당 파일 저장

class Document(models.Model):         # 문서 파일
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):        # 이미지 파일
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
