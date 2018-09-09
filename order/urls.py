"""
URL manager for the Order app
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url('order', views.OrderListCreate.as_view() , name='order'),
]