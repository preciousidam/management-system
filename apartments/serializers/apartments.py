from rest_framework import serializers


from apartments.models import Apartment, Tenancy


class TenancySerializer(serializers.ModelSerializer):
    tenant_name = serializers.CharField(read_only=True)
    class Meta:
        model=Tenancy
        fields = '__all__'


class SimilarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Apartment
        fields=['id', 'flat', 'building', 'no_of_bed']

class ApartmentSerializer(serializers.ModelSerializer):
    current_tenancy_period = TenancySerializer(read_only=True)
    all_tenancy_period = TenancySerializer(many=True, read_only=True)
    get_tenant = serializers.CharField(read_only=True)
    get_landlord = serializers.CharField(read_only=True)
    similar = SimilarSerializer(many=True, read_only=True)

    class Meta:
        model=Apartment
        fields = '__all__'

