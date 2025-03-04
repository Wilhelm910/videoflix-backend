from rest_framework import serializers
from users_app.models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "password", "is_verified", "last_name", "first_name"]
        # Ensure the password is write-only.
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        # Remove the password to handle it separately.
        password = validated_data.pop('password', None)
        # Create the user with the provided data and set the password.
        user = CustomUser.objects.create_user(**validated_data, password=password)
        return user
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True, style={'input_type': 'password'}, trim_whitespace=False
    )

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            # Attempt to authenticate the user.
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
        # Check if the old password matches the user's current password.
        if not user.check_password(value):
            raise serializers.ValidationError("Old password is not correct")
        return value
    
    
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        # Ensure a user with the provided email exists.
        try:
            CustomUser.objects.get(email=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def save(self):
        # Generate a password reset token and assign it to the user.
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
        # Validate the reset token by ensuring a user exists with it.
        try:
            CustomUser.objects.get(password_reset_token=value)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Invalid or expired token.")
        return value

    def save(self):
        # Reset the user's password and clear the token.
        token = self.validated_data['token']
        new_password = self.validated_data['new_password']
        user = CustomUser.objects.get(password_reset_token=token)
        user.set_password(new_password)
        user.password_reset_token = None  # Remove the reset token after use.
        user.save()
        return user
