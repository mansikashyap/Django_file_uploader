from rest_framework import serializers
from rest_famework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser, File




class CustomTokenObtainOairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self,validated_data):
            user = CustomUser.objects.create_user(**validated_data)
            return user