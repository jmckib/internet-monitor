from django.db import models


class PingRecord(models.Model):
    """Record of a successful google.com ping on wifi device."""
    when_created = models.DateTimeField(auto_now_add=True)


class SpeedRecord(models.Model):
    """Record of speed in KB/s from wgetting 10 MB file on wifi device."""
    when_created = models.DateTimeField(auto_now_add=True)
    kb_per_second = models.PositiveIntegerField()
