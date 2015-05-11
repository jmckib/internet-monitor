from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import PingRecord


@csrf_exempt
def record_ping_view(request):
    if request.method == 'POST':
        PingRecord.objects.create()
        return JsonResponse({'success': True})