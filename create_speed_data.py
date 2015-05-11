from datetime import timedelta
import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uptime.settings")

# your imports, e.g. Django models
from stats.models import SpeedRecord
from stats.views import utc_now

# From now onwards start your script..
now = utc_now()
for num_hours in range(25):
    rec = SpeedRecord.objects.create(
        kb_per_second=random.randint(1100, 12000))
    rec.when_created = now - timedelta(hours=num_hours)
    rec.save()
