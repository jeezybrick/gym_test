from django.db import models
from django.conf import settings


class Booking(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='booking')
    swim_lane = models.SmallIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.user
