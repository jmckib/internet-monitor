from django.db import models


class PingRecord(models.Model):
    """Record of a successful google.com Ping on wifi-enabled device."""
    when_created = models.DateTimeField(auto_now_add=True)
