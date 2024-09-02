from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser
from users.serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token

User = get_user_model()

class CustomUserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword'
        )

    def test_user_creation(self):
        """Test the creation of a CustomUser object"""
        user = User.objects.get(email='test@example.com')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertFalse(user.is_verified)
        self.assertIsNotNone(user.email_verification_token)

    def test_superuser_creation(self):
        """Test the creation of a superuser"""
        superuser = User.objects.create_superuser(
            email='superuser@example.com',
            password='superpassword'
        )
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.check_password('superpassword'))
        
        
class RegisterUserViewTest(APITestCase):

    def setUp(self):
        self.url = reverse('register')  # URL-Namen sicherstellen
    
    def test_register_user(self):
        """Test the registration of a new user."""
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, 'testuser@example.com')

    def test_register_user_invalid(self):
        """Test the registration with invalid data."""
        data = {
            'email': 'invalid-email',  # Invalid email format
            'password': 'short'        # Invalid password (assuming there's a minimum length requirement)
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Check that the email error is present
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'][0], 'Enter a valid email address.')

        # If password errors are also expected, ensure you check for them
        if 'password' in response.data:
            self.assertIn('password', response.data)
            self.assertEqual(response.data['password'][0], 'This field is required.')  # Example error message, adjust as needed
            
            
class CustomUserViewTest(APITestCase):

    def setUp(self):
        # Erstellen von Benutzern
        self.user1 = CustomUser.objects.create_user(email='user1@example.com', password='testpassword1')
        self.user2 = CustomUser.objects.create_user(email='user2@example.com', password='testpassword2')
        
        # Erstellen eines Tokens für Authentifizierung
        self.token = Token.objects.create(user=self.user1)
        self.auth_header = 'Token ' + self.token.key
        
        # URL für die Abfrage aller Benutzer
        self.url = reverse('get-all-users')  

    def test_get_users_authenticated(self):
        """Test the GET request for retrieving users when authenticated."""
        response = self.client.get(self.url, HTTP_AUTHORIZATION=self.auth_header)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Prüfe, ob die Benutzer in der Antwort enthalten sind
        self.assertEqual(len(response.data), 2)
        self.assertIn('user1@example.com', [user['email'] for user in response.data])
        self.assertIn('user2@example.com', [user['email'] for user in response.data])

    def test_get_users_unauthenticated(self):
        """Test the GET request for retrieving users when not authenticated."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Prüfe, ob die Benutzer in der Antwort enthalten sind
        self.assertEqual(len(response.data), 2)
        self.assertIn('user1@example.com', [user['email'] for user in response.data])
        self.assertIn('user2@example.com', [user['email'] for user in response.data])