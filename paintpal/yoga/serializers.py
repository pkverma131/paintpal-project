from rest_framework import serializers
from .models import YogaPath, Yogasana


class YogasanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yogasana
        fields = '__all__'

class YogaPathSerializer(serializers.ModelSerializer):
    yogasanas = YogasanaSerializer(many=True, read_only=True)

    class Meta:
        model = YogaPath
        fields = ['id', 'name', 'description', 'yogasanas']

