from django.http import JsonResponse
from django.core.cache import cache
from .models import Product
from django.core.serializers import serialize

def product_list(request):            # 전체 캐싱
    cache_key = 'full_product_list'   # 캐시 키 정의
    cached_data = cache.get(cache_key)    # 캐시에서 데이터를 가져옴
    if cached_data:
        return JsonResponse(cached_data, safe=False)
    products = list(Product.objects.all().values('id', 'name', 'price', 'is_featured'))
    cache.set(cache_key, products, timeout=3600)      # 캐시에 상품 목록 저장 및 시간 설정
    return JsonResponse(products, safe=False)

def featured_products(request):       # 부분 캐싱
    cache_key = 'featured_product_list'   # 캐시 키 정의
    cached_data = cache.get(cache_key)    # 캐시에서 데이터를 가져옴
    if cached_data:
        return JsonResponse(cached_data, safe=False)
    products = list(Product.objects.filter(is_featured=True).values('id', 'name', 'price'))   # 필터링 (조건을 사용하여 해당 상품 -> 부분)
    cache.set(cache_key, products, timeout=120)
    return JsonResponse(products, safe=False)