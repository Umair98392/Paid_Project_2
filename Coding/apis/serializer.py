from rest_framework import serializers 
from api.models import localityDescription
 
 
class localityDescriptionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = localityDescription
        fields = (
                  'Id',
                  'MSSubClass',
                  'MSZoning',
                  'LotFrontage',
                  'LotArea',
                  'Street',
                  'Alley',
                  'LotShape',
                  'LandContour',
                  'Utilities',
                  'LotConfig',
                  'LandSlope',
                  'Neighborhood')
