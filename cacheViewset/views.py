from rest_framework.viewsets import ModelViewSet
from django.core.cache import cache
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response



"""
A viewset that provides default `create()`, `retrieve()`, `update()`,
`partial_update()`, `destroy()` and `list()` actions.
"""


class ProductViewSet(ModelViewSet):       # 함수가 아닌 ViewSet을 사용 <- 오버라이딩 필요로함
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):     # 전체캐싱
        cache_key = 'full_product_list'
        cached_data = cache.get(cache_key)    # 해당 캐시 키에 해당하는 데이터 캐싱
        if cached_data:
            return Response(cached_data)
        
        # 캐시된 데이터가 없는 경우, 부모 클래스인 ModelViewSet의 list 메서드를 호출하여 (super) 원래의 동작 수행
        # DB에서 상품 목록을 가져옴
        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=1200)   # 캐시에 저장
        return response

    def retrieve(self, request, *args, **kwargs):     # 부분캐싱
        obj = self.get_object()         # 상품 객체 가져옴
        cache_key = f'product_{obj.pk}'     # 상품 객체의 PK를 사용하여 캐시 키 생성
        cached_data = cache.get(cache_key)        # 해당 정보 캐시에 저장
        if cached_data:
            return Response(cached_data)
        response = super().retrieve(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=1200)
        return response