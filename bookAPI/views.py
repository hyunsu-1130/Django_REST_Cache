from rest_framework.viewsets import ModelViewSet
from django.core.cache import cache
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response

class BookViewSet(ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

  def list(self, request, *args, **kwargs):     # 책 목록 조회
    cache_key = 'book_list'     # 캐시 키 생성
    cached_data = cache.get(cache_key)       # 캐시 키로부터 캐시 데이터 가져오기
    if cached_data is not None:        # 캐시 데이터가 있다면
      return Response(cached_data)
    
      # 캐시된 데이터가 없는 경우, 부모 클래스인 ModelViewSet의 list 메서드를 호출하여 (super) 원래의 동작 수행
      # DB에서 상품 목록을 가져옴
    response = super().list(request, *args, **kwargs) 
    cache.set(cache_key, response.data, timeout=600)    # 10분간 캐시 값 유지
    return response
  
  def create(self, request, *args, **kwargs):         # 새 책이 추가되면 캐시를 삭제하여 갱신
    cache.delete('book_list')   # 캐시 키 값을 삭제
    return super().create(request, *args, **kwargs)
  
  def update(self, request, *args, **kwargs):   # 기존 책이 수정되면 캐시를 삭제하여 갱신
    cache.delete('book_list')
    return super().update(request, *args, **kwargs)
  
  def destroy(self, request, *args, **kwargs):
    cache.delete('book_list')     # 책이 삭제되면 캐시를 삭제하여 갱신
    return super().destroy(request, *args, **kwargs)