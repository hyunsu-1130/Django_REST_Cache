from django.core.cache import cache
from django.http import JsonResponse
from .models import Event

def event_list(request):
    # 캐시에서 이벤트 목록 가져오기
    events = cache.get('events')      # events라는 키를 가져와
    if not events:
        events = list(Event.objects.all().values('name', 'date'))
        cache.set('events', events, timeout=60)  # 5분 동안 캐시 유지
    return JsonResponse(events, safe=False)