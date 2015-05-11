from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import PingRecord
from .models import SpeedRecord


@csrf_exempt
def record_ping_view(request):
    if request.method == 'POST':
        PingRecord.objects.create()
        return JsonResponse({'success': True})


@csrf_exempt
def record_speed_view(request):
    if request.method == 'POST':
        SpeedRecord.objects.create(kb_per_second=request.POST['kb_per_second'])
        return JsonResponse({'success': True})
