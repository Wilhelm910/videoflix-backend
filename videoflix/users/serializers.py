from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "password", "is_verified", "last_name", "first_name"]
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
         # Entferne das Passwort aus den validierten Daten, um es separat zu behandeln
        password = validated_data.pop('password', None)
        
        # Erstelle den Benutzer über den CustomUserManager und setze das Passwort
        user = CustomUser.objects.create_user(**validated_data, password=password)
        return user