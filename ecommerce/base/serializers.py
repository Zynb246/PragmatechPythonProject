from rest_framework import serializers
from product.models import Product,ProductFile
from brand.models import Brand
from category.models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    class Meta:
        model = SubCategory
        fields = '__all__'

class BrandSerializers(serializers.ModelSerializer):
    sub_category = SubCategorySerializers(read_only=True)
    class Meta:
        model = Brand
        exclude = ['brand_slug',]

class ProductFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductFile
        exclude = ['product',]


#
class ProductList(serializers.ListSerializer):
    def to_representation(self,data):
        qs = self.context['request'].GET.get('category')
        data = data.filter()
        return super().to_representation(data)
#
class ProductPrice(serializers.Field):
    def to_representation(self, value):
        price_list = {
            "ilk qiymet": value.product_price,
            "endirim_faizi": value.product_discount,
            "endirimli_qiymeti": value.product_discount_price
        }
        return price_list

class ProductSerializers(serializers.ModelSerializer):
    product_price_list= ProductPrice(source="*")
    category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        exclude = ['product_price', 'product_discount',"product_discount_price", ]
    
    def get_category(self,obj):
        ids = obj.product_brand.sub_category.category.id
        category = obj.product_brand.sub_category.category.name
        data = {
            'id':ids,
            'category_name':category
        }
        return data

class ProductDetailSerializers(serializers.ModelSerializer):
    product_brand = BrandSerializers(read_only=True)
    productfile_set = ProductFileSerializers(many=True)
    class Meta:
        model = Product
        fields = '__all__'