from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users_app.serializers import ChangePasswordSerializer, CustomUserSerializer, LoginSerializer, PasswordResetConfirmSerializer, PasswordResetSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from users_app import serializers
from .models import CustomUser
from .utils import send_password_reset_email, send_verification_email
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

class RegisterUserView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
          #  print(f"Token after user creation: {user.email_verification_token}")
            send_verification_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    permission_classes = [AllowAny] 
    def get(self, request, token, format=None):
        print(f"Received token: {token}")  # Debug-Ausgabe
        try:
            user = get_object_or_404(CustomUser, email_verification_token=token)
            print(f"User's token: {user.email_verification_token}")  # Debug-Ausgabe
            if user.is_verified:
                print("E-Mail wurde bereits verifiziert.")  # Debug-Ausgabe
                return Response({"message": "E-Mail wurde bereits verifiziert."}, status=status.HTTP_400_BAD_REQUEST)
            if user.email_verification_token == token:
                print("Token stimmt überein, verifiziere Benutzer...")  # Debug-Ausgabe
                user.is_verified = True
                
                user.save()
                user.email_verification_token = ''
                print("Benutzer erfolgreich verifiziert und gespeichert.")  # Debug-Ausgabe
                return Response({"message": "E-Mail erfolgreich verifiziert."}, status=status.HTTP_200_OK)
            print("Ungültiger Token.")  # Debug-Ausgabe
            return Response({"message": "Ungültiger Token."}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            print("Benutzer nicht gefunden.")  # Debug-Ausgabe
            return Response({"message": "Benutzer nicht gefunden."}, status=status.HTTP_404_NOT_FOUND)

    
class CustomUserView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    
class UserLoginView(ObtainAuthToken):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        print('Received login request. Data:', request.data)
        serializer = self.serializer_class(data=request.data,context={'request': request})
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request=request, username=email, password=password)
            if user:
                if not user.is_verified:
                    # Benutzer ist nicht verifiziert
                    return Response(
                        {"error": "User is not verified. Please verify your email."},
                        status=status.HTTP_403_FORBIDDEN
                    )
                token, created = Token.objects.get_or_create(user=user)
                response_data = {
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email,
                    'is_verified': user.is_verified
                }
                return Response(response_data)
            else:
                return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Invalid input. Please check your email and password.'}, status=status.HTTP_400_BAD_REQUEST)
        
        
@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        try:
            if hasattr(request.user, 'auth_token'):
                request.user.auth_token.delete()
            else:
                print("No auth_token found for user:", request.user)  # Debugging-Ausgabe
                return Response({'error': 'Invalid token or user not authenticated'}, status=status.HTTP_400_BAD_REQUEST)
        except AttributeError:
            print("AttributeError: User not authenticated")  # Debugging-Ausgabe
            return Response({'error': 'Invalid token or user not authenticated'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'success': 'Logged out successfully'}, status=status.HTTP_200_OK)
    
    
    
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request,format=None):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
class PasswordResetView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Benutzer wird mit Token aktualisiert
            send_password_reset_email(user)  # E-Mail senden
            return Response({"message": "Password reset email sent."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request, *args, **kwargs):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password reset successful."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

