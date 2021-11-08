from rest_framework import serializers
from .models import *


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
        exclude = ('block',)


class GetBlockSerializer(serializers.ModelSerializer):
    contents = GetContentSerializer(many=True)

    class Meta:
        depth = 1
        model = Block
        exclude = ('page',)


class GetPageSerializer(serializers.ModelSerializer):
    blocks = GetBlockSerializer(many=True)

    class Meta:
        depth = 1
        model = Page
        fields = '__all__'

# остальной контент

class GetNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class GetVacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'


class GetClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class GetPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class GetHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
