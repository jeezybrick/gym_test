
from django.http import Http404
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from rest_framework import generics, status, permissions, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from my_auth.models import MyUser
from booking.models import Booking, BookingTimeStep
from api import serializers


# Standard Pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 1


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.order_by('start_date')
    serializer_class = serializers.BookingSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        send_mail('Subject here', 'Here is the message.', 'smooker14@gmail.com',
        ['tsmooker14@gmail.com'], fail_silently=False)
        return self.create(request, *args, **kwargs)


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (permissions.IsAuthenticated, )


class BookingTimeStepList(generics.GenericAPIView):
    serializer_class = serializers.BookingTimeStepSerializer
    queryset = BookingTimeStep.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        queryset = BookingTimeStep.objects.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.BookingTimeStepSerializer(queryset, many=True)
        return Response(serializer.data)
