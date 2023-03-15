from rest_framework import serializers
from .models import category


class categorySerial(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

