from django.db import models
from django.conf import settings


class Booking(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='booking')
    swim_lane = models.SmallIntegerField()
    start_date = models.DateField()
    start_time = models.TimeField()

    def __str__(self):
        return self.user


class BookingTimeStep(models.Model):
    time_start = models.TimeField()
    time_end = models.TimeField()

    def __str__(self):
        return self.time
