from rest_framework import serializers

from apartments.models import Agreement

class AgreementSerializer(serializers.ModelSerializer):

    class Meta:
        model=Agreement
        fields = '__all__'