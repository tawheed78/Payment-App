from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'phone_number': {'required': True},
            }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    