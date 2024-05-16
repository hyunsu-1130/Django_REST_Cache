from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['title', 'author', 'published_date', 'isbn_number', 'page_count', 'review_count'] 