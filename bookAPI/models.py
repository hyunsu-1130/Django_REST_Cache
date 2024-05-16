from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  published_date = models.DateField()
  isbn_number = models.DateField(max_length=20)
  page_count = models.IntegerField()
  review_count = models.IntegerField(default=0)