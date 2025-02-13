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
    img = serializers.SerializerMethodField()
    
    class Meta:
        model = SliderProd
        exclude = ('product',)
    
    def get_img(self, obj):
        if obj.img:
            return obj.img.url
        return None


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
    img = serializers.SerializerMethodField()
    
    class Meta:
        model = Solution
        exclude = ('product',)
    
    def get_img(self, obj):
        if obj.img:
            return obj.img.url
        return None


class ItemsExampleSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    
    class Meta:
        model = ItemsExample
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    ItemsExample = ItemsExampleSerializer(many=True)

    class Meta:
        model = Items
        exclude = ('product',)
        
    def get_img(self, obj):
        if obj.img:
            return obj.img.url
        return None


class FilterSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    
    class Meta:
        model = Filters
        fields = '__all__'

    def get_img(self, obj):
        if obj.img:
            return obj.img.url
        return None


class CategoryFilterSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    Filters = FilterSerializer(many=True)

    class Meta:
        model = CategoryFilters
        fields = '__all__'

    def get_img(self, obj):
        if obj.img:
            return obj.img.url
        return None


class PacketOptionsSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    
    class Meta:
        model = PacketOptions
        fields = '__all__'
        
    def get_img(self, obj):
        if obj.img:
            return obj.img.url
        return None


class PacketSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    drawing = serializers.SerializerMethodField()
    
    class Meta:
        model = Packet
        fields = '__all__'
        
    def get_img(self, obj):
        if obj.img:
            return obj.img.url
        return None
    
    def get_drawing(self, obj):
        if obj.drawing:
            return obj.drawing.url
        return None


class PacketSeamSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    
    class Meta:
        model = PacketSeam
        fields = '__all__'
        
    def get_img(self, obj):
        if obj.img:
            return obj.img.url
        return None


class ClientSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = '__all__'

    def get_logo(self, obj):
        if obj.logo:
            return obj.logo.url
        return None

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
