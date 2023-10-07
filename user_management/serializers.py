# usermanagement/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            # Add more fields from your User model as needed
        )

        extra_kwargs = {
            'password': {'write_only': True},  # Password should not be read when retrieving data
            'email': {'required': True},         # Email is required during user creation
        }

    def create(self, validated_data):
        # Create a new user with the validated data, including hashing the password
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data.get('phone_number', ''),
            # Add more fields here
        )
        return user
