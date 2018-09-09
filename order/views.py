from django.shortcuts import render
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework import generics

class OrderListCreate(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer