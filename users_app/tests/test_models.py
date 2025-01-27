from django.test import TestCase
from users_app.models import CustomUser


class CustomUserModelTests(TestCase):

    def test_create_user(self):
        """Test, ob ein normaler Benutzer erstellt werden kann."""
        email = "user@example.com"
        password = "testpassword123"
        user = CustomUser.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertIsNotNone(user.email_verification_token)  # Prüfen, ob ein Verifizierungs-Token generiert wurde

    def test_create_user_without_email_raises_error(self):
        """Test, ob ein ValueError ausgelöst wird, wenn keine E-Mail-Adresse angegeben ist."""
        with self.assertRaises(ValueError) as context:
            CustomUser.objects.create_user(email=None, password="password123")
        self.assertEqual(str(context.exception), 'Der Benutzer muss eine E-Mail-Adresse haben.')

    def test_create_superuser(self):
        """Test, ob ein Superuser korrekt erstellt wird."""
        email = "admin@example.com"
        password = "adminpassword123"
        superuser = CustomUser.objects.create_superuser(email=email, password=password)

        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.check_password(password))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_verification_token_is_generated_on_save(self):
        """Test, ob ein Verifizierungs-Token bei der Erstellung eines neuen Benutzers generiert wird."""
        user = CustomUser.objects.create_user(email="user2@example.com", password="password123")
        self.assertIsNotNone(user.email_verification_token)

    def test_generate_password_reset_token(self):
        """Test, ob das Passwort-Reset-Token korrekt generiert wird."""
        user = CustomUser.objects.create_user(email="user3@example.com", password="password123")
        reset_token = user.generate_password_reset_token()
        self.assertIsNotNone(reset_token)
        self.assertEqual(len(reset_token), 27)  # `secrets.token_urlsafe(20)` erzeugt standardmäßig 27 Zeichen

    def test_string_representation(self):
        """Test, ob die String-Repräsentation des Benutzers korrekt ist."""
        user = CustomUser.objects.create_user(email="user4@example.com", password="password123")
        self.assertEqual(str(user), user.email)
