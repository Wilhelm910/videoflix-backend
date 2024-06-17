from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import CustomUserSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from users import serializers
from .models import CustomUser
from .utils import send_verification_email

class RegisterUserView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(f"Token after user creation: {user.email_verification_token}")
            send_verification_email(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    def get(self, request, token, format=None):
        print(f"Received token: {token}")  # Debug-Ausgabe
        user = get_object_or_404(CustomUser, email_verification_token=token)
        print(f"User's token: {user.email_verification_token}")
        if user.is_verified:
            return Response({"message": "E-Mail wurde bereits verifiziert."}, status=status.HTTP_400_BAD_REQUEST)
        if user.email_verification_token == token:
            user.is_verified = True
            user.email_verification_token = ''
            user.save()
            return Response({"message": "E-Mail erfolgreich verifiziert."}, status=status.HTTP_200_OK)
        return Response({"message": "Ungültiger Token."}, status=status.HTTP_400_BAD_REQUEST)
    
    
class CustomUserView(APIView):
    def get(self, request, format=None):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    
class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print('Received login request. Data:', request.data)
        serializer = self.serializer_class(data=request.data,context={'request': request})
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request=request, username=email, password=password)
            print("TEST")
            if user:
                token, created = Token.objects.get_or_create(user=user)
                response_data = {
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email
                }
                return Response(response_data)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)