from rest_framework import serializers
from billing.models import BillingProfile
from order.models import Order
from backend.models import User
from cart.models import Cart,CartProduct
from base.serializers import ProductSerializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class TokenPairSerializers(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super(TokenPairSerializers,cls).get_token(user)
        token['username'] = user.username
        return token 

class RegisterSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = User
        fields = ['username','password','password2','email','last_name','first_name',]
        extra_kwargs = {
            'first_name': {"required":True},
            'last_name' : {"required":True}
        }
    
    def validate(self, attrs):
        if attrs['password'] !=attrs['password2']:
            raise serializers.ValidationError({'password':"sifrede yalnisliq var"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            last_name = validated_data['last_name'],
            first_name = validated_data['first_name'],
            #password = validated_data['password'],
        )
 
        user.set_password(validated_data['password'])
        user.save()
        return user

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



