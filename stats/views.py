from datetime import datetime
import pytz

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import PingRecord
from .models import SpeedRecord


def utc_now():
    return datetime.utcnow().replace(tzinfo=pytz.utc)


def index_view(request):
    latest_ping = PingRecord.objects.latest()
    is_down = (utc_now() - latest_ping.when_created).seconds > 40

    context = {
        'is_down': is_down,
    }

    return render(request, 'index.html', context)


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
