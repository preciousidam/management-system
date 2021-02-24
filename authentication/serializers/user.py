from rest_framework import serializers

from authentication.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=User
        fields= ['url','email', 'password', 'first_name', 'last_name', 'phone', 'pk', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data.pop('email')
        user = User(is_staff=False, is_superuser=False, is_active=True, email=email.lower(), **validated_data)
        user.set_password(password)
        user.save()
        return user