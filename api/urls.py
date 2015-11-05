
from django.conf.urls import url
from api import views


urlpatterns = [
    url(r'^api/booking/$', views.BookingList.as_view(), name='booking_list_api'),
    url(r'^api/booking/(?P<pk>[0-9]+)/$',
        views.BookingDetail.as_view(), name='booking_detail_api'),

]
