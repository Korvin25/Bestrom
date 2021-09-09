from rest_framework import serializers
from .models import Product, ProductProperties, ProductPropertyValue, SliderProd, Items, ItemsExample, Equipment, \
    Solution, Docs


# для списка товаров
class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# получение карточки товара
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperties
        exclude = ('product',)


class PropertyValueSerializer(serializers.ModelSerializer):
    product_property = PropertySerializer()

    class Meta:
        model = ProductPropertyValue
        exclude = ('product',)


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderProd
        exclude = ('product',)


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        exclude = ('product',)


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        exclude = ('product',)


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        exclude = ('product',)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        exclude = ('product',)


class DetailProductSerializer(serializers.ModelSerializer):
    ProductPropertyValue = PropertyValueSerializer(many=True)
    SliderProd = SliderSerializer(many=True)
    Items = ItemSerializer(many=True)
    Docs = DocSerializer(many=True)
    Equipment = EquipmentSerializer(many=True)
    Solution = SolutionSerializer(many=True)

    class Meta:
        depth = 1
        model = Product
        fields = '__all__'
