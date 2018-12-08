from rest_framework.serializers import ModelSerializer
from core.models import Attraction


class AttractionSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('id', 'name', 'description', 'operating_hours', 'min_age')
