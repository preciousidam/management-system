from rest_framework import serializers


from contacts.models import Client, Vendor


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields = '__all__'



class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields = '__all__'
