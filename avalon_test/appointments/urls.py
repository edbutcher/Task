from django.conf.urls import url
from . import views

app_name = 'appointments'

urlpatterns = [
    url(r'^$', views.ListAppointment.as_view(), name='all'),
    url(r'^new/$', views.CreateAppointment.as_view(), name='create'),
    url(r'appointment/in/(?P<slug>[-\w]+)/$', views.SingleAppointment.as_view(), name='single'),
    url(r'join/(?P<slug>[-\w]+)/$', views.JoinAppointment.as_view(), name='join'),
    url(r'leave/(?P<slug>[-\w]+)/$', views.LeaveAppointment.as_view(), name='leave'),

]