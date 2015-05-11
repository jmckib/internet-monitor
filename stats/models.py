from django.db import models


class CreateRecord(models.Model):
    class Meta:
        abstract = True
        get_latest_by = 'when_created'

    when_created = models.DateTimeField(auto_now_add=True)


class PingRecord(CreateRecord):
    """Record of a successful google.com ping on wifi device."""


class SpeedRecord(CreateRecord):
    """Record of speed in KB/s from wgetting 10 MB file on wifi device."""
    kb_per_second = models.PositiveIntegerField()
