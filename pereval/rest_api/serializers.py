from .models import *
from rest_framework import serializers


class PerevalAddedSerializer(serializers.HyperlinkedModelSerializer):
    ...


class PerevalAreasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PerevalAreas

















