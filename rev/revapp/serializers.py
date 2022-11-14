from rest_framework import serializers
# from .models import Message,GroupDetails,GroupName
from django.contrib.auth.models import User
# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password','email']





class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError('email already exists')
        return super().validate(attrs)