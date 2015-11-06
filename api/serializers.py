from rest_framework import serializers
from my_auth.models import MyUser
from booking.models import Booking, BookingTimeStep


class UserSerializer(serializers.ModelField):

    class Meta:
        model = MyUser
        fields = ('url', 'username', 'email', 'is_staff', )


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('id', 'swim_lane', 'start_date', 'start_time', 'end_time', )


class BookingTimeStepSerializer(serializers.ModelSerializer):

    is_booked = serializers.SerializerMethodField(read_only=True)

    def get_is_booked(self, obj):
        request = self.context.get('request', None)
        return Booking.objects.filter(start_time=obj.time_start).exists()

    class Meta:
        model = BookingTimeStep
        fields = ('id', 'time_start', 'time_end', 'is_booked', )
