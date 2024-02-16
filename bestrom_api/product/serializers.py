from rest_framework import serializers

from .models import *
from content.models import Client


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
    SliderProd = SliderSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'SliderProd', 'name', 'name_en')


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        exclude = ('product',)


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        exclude = ('product',)


class ItemsExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsExample
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    ItemsExample = ItemsExampleSerializer(many=True)

    class Meta:
        model = Items
        exclude = ('product',)


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filters
        fields = '__all__'


class CategoryFilterSerializer(serializers.ModelSerializer):
    Filters = FilterSerializer(many=True)

    class Meta:
        model = CategoryFilters
        fields = '__all__'


class PacketOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketOptions
        fields = '__all__'


class PacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packet
        fields = '__all__'

    def to_representation(self, instance):
        if instance.active:
            return super().to_representation(instance)
            

class PacketOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketOptions
        fields = '__all__'


class PacketSeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketSeam
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class DetailProductSerializer(serializers.ModelSerializer):
    ProductPropertyValue = PropertyValueSerializer(many=True)
    SliderProd = SliderSerializer(many=True)
    Items = ItemSerializer(many=True)
    Docs = DocSerializer(many=True)
    equipments = EquipmentSerializer(many=True)
    Solution = SolutionSerializer(many=True)
    Packet = PacketSerializer(many=True)
    PacketsOptions = PacketOptionsSerializer(many=True)
    clients = ClientSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
