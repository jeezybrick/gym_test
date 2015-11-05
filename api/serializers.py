from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from my_auth.models import MyUser
from booking.models import Booking, BookingTimeStep


class UserSerializer(serializers.ModelField):

    class Meta:
        model = MyUser
        fields = ('url', 'username', 'email', 'is_staff', )


class BookingSerializer(serializers.ModelSerializer):

    test = serializers.SerializerMethodField(read_only=True)

    def get_test(self, obj):
        return [datetime(2012, 1, 1, hr, min, 0).time() for hr in range(9, 22) for min in range(0,60,30)]

    class Meta:
        model = Booking
        fields = ('id', 'user', 'swim_lane', 'start_date', 'start_time', 'test',)


class BookingTimeStepSerializer(serializers.ModelSerializer):

    is_booked = serializers.SerializerMethodField(read_only=True)

    def get_is_booked(self, obj):
        request = self.context.get('request', None)
        return Booking.objects.filter(start_time=obj.time).exists()

    class Meta:
        model = BookingTimeStep
        fields = ('id', 'time', 'is_booked', )
