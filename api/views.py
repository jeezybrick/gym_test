
from django.http import Http404
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, status, permissions, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from my_auth.models import MyUser
from booking.models import Booking
from api import serializers


# Standard Pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 1


# Comments pagination
class CommentsSetPagination(StandardResultsSetPagination):
    page_size = 4


class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Item detail
class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
