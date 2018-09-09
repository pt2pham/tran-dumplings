from rest_framework import serializers
from order.models import Order

'''
Serializer for the Order class
'''
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'