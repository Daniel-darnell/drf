# Serializers define the representation of our model in JSON format and convert object instances to a more transferrable format. This will simply the parsing of data of our api. Deserializers do the opposite.
from rest_framework import serializers
from .models import CartItem

class CartItemSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatFieldI()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')