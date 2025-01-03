from rest_framework import serializers
from users_app.models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


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
    
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value
    
    
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = CustomUser.objects.get(email=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def save(self):
        email = self.validated_data['email']
        user = CustomUser.objects.get(email=email)
        token = user.generate_password_reset_token()
        user.password_reset_token = token
        user.save()
        return user
    

class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(validators=[validate_password])

    def validate_token(self, value):
        try:
            user = CustomUser.objects.get(password_reset_token=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Invalid or expired token.")
        return value

    def save(self):
        token = self.validated_data['token']
        new_password = self.validated_data['new_password']
        user = CustomUser.objects.get(password_reset_token=token)
        user.set_password(new_password)
        user.password_reset_token = None  # Reset token entfernen
        user.save()
        return user

