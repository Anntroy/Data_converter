from rest_framework import serializers
from location_register.models.ratu_models import Region, District, City, CityDistrict, Street


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name', 'koatuu')


class DistrictSerializer(serializers.ModelSerializer):
    region = serializers.CharField(max_length=30)

    class Meta:
        model = District
        fields = ('id', 'region', 'name', 'koatuu')


class CitySerializer(serializers.ModelSerializer):
    region = serializers.CharField(max_length=30)
    district = serializers.CharField(max_length=100)

    class Meta:
        model = City
        fields = ('id', 'region', 'district', 'name', 'koatuu')


class CityDistrictSerializer(serializers.ModelSerializer):
    region = serializers.CharField(max_length=30)
    district = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)

    class Meta:
        model = CityDistrict
        fields = ('id', 'region', 'district', 'city', 'name', 'koatuu')


class StreetSerializer(serializers.ModelSerializer):
    region = serializers.CharField(max_length=30)
    district = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    citydistrict = serializers.CharField(max_length=100)

    class Meta:
        model = Street
        fields = ('id', 'region', 'district', 'citydistrict', 'city', 'name')