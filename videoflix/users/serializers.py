from rest_framework import serializers
from users.models import CustomUser
from django.contrib.auth import authenticate


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
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            # Versuche, den Benutzer zu authentifizieren
            user = authenticate(username=email, password=password)
            if user is None:
                raise serializers.ValidationError("Invalid email or password.")
            if not user.is_active:
                raise serializers.ValidationError("User is inactive.")

        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        data['user'] = user
        return data