from django.contrib.auth import get_user_model #32
from rest_framework import serializers #33

User = get_user_model() #34

class UserSerializer(serializers.ModelSerializer): #35
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'profile_picture', 'description']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data): #36 -> views.py
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            profile_picture=validated_data.get('profile_picture'),
            description=validated_data.get('description')
        )
        return user