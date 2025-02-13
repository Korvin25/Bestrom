from rest_framework import serializers
from .models import *
from product.serializers import DetailProductSerializer


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = ContFile
        fields = '__all__'

    def get_file_url(self, file):
        request = self.context.get('request')
        file_url = file.photo.url
        return request.build_absolute_uri(file_url)


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class GetContentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Content
        exclude = ('block', 'active')

    def to_representation(self, instance):
        if instance.active:
            return super().to_representation(instance)
        return {}


class GetBlockSerializer(serializers.ModelSerializer):
    contents = GetContentSerializer(many=True)

    class Meta:
        depth = 1
        model = Block
        exclude = ('page',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['contents'] = [
            content for content in representation['contents'] if content
        ]
        return representation


class GetPageSerializer(serializers.ModelSerializer):
    blocks = GetBlockSerializer(many=True)

    class Meta:
        depth = 1
        model = Page
        fields = '__all__'


# остальной контент

class GetNewsSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    
    class Meta:
        model = News
        fields = '__all__'


class GetVacancySerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    
    class Meta:
        model = Vacancy
        fields = '__all__'


class GetClientSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    Product = DetailProductSerializer(many=True)

    class Meta:
        model = Client
        fields = '__all__'


class GetPartnerSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    
    class Meta:
        model = Partner
        fields = '__all__'


class GetHistorySerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()
    
    class Meta:
        model = History
        fields = '__all__'
