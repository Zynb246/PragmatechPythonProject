from rest_framework import serializers
from billing.models import BillingProfile
from order.models import Order
from backend.models import User
from cart.models import Cart,CartProduct
from base.serializers import ProductSerializers

class CartProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = "__all__"

class CartSerializers(serializers.ModelSerializer):
    products = CartProductSerializers(many=True)
    class Meta:
        model = Cart
        exclude = ['user']

class OrderSerialziers(serializers.ModelSerializer): 
    cart = CartSerializers(read_only=True)
    class Meta:
        model = Order
        exclude =["billing_profile","shipping_address","billing_address",]
   
class BillingProfileSerializers(serializers.ModelSerializer):
    billing_profile=OrderSerialziers(many=True,read_only=True)
    class Meta :
        model = BillingProfile
        exclude = ["user",]

class UserSerializers(serializers.ModelSerializer):
    billing_user=BillingProfileSerializers()
    class Meta:
        model = User
        fields = ["billing_user",]



