from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    """
        This class used to serialize input data
    """
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'validators': (validate_password,), 'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'error': 'password fields did not match.'})
        return attrs

    def validate_email(self, value):
        user = User.objects.filter(email=value)
        if user:
            raise serializers.ValidationError({'error':'This email already exist'})
        return value

    def create(self, validated_data):
        del validated_data['password2']
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

        