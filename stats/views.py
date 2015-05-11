from datetime import datetime
from datetime import timedelta
import pytz

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import PingRecord
from .models import SpeedRecord

DOWN_SECONDS_THRESHOLD = 40


def utc_now():
    return datetime.utcnow().replace(tzinfo=pytz.utc)


def index_view(request):
    latest_ping_record = PingRecord.objects.latest()
    is_down = ((utc_now() - latest_ping_record.when_created).seconds
               > DOWN_SECONDS_THRESHOLD)

    speed_records = (SpeedRecord.objects
                     .filter(when_created__gt=utc_now() - timedelta(hours=24))
                     .order_by('when_created'))
    speed_data = [
        {'date': rec.when_created.isoformat(),
         'mb_per_second': rec.mb_per_second}
        for rec in speed_records]

    context = {
        'is_down': is_down,
        'latest_speed_record': SpeedRecord.objects.latest(),
        'speed_data': speed_data,
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
