from django.test import TestCase

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from users.models import CustomUser

class VerifyEmailTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='password',
            email_verification_token='testtoken'
        )
    
    def test_verify_email(self):
        response = self.client.get(f'/verify-email/{self.user.email_verification_token}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_verified)

