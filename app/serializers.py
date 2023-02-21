from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
)
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Plot


class ListSerializer(ModelSerializer):
    class Meta:
        model = Plot
        fields = [
            'farmer',
            'culture',
            'season',
            'contour',
        ]


class PlotSerializer(GeoFeatureModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Plot
        geo_field = 'contour'
        fields = ['id', 'culture', 'season']
