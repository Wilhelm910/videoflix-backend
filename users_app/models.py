from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import secrets

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Ensure the email is provided.
        if not email:
            raise ValueError('Der Benutzer muss eine E-Mail-Adresse haben.')
        # Normalize the email and use it as the username.
        email = self.normalize_email(email)
        extra_fields['username'] = email
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Set default flags for superuser.
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    email_verification_token = models.CharField(max_length=50, blank=True, null=True)
    password_reset_token = models.CharField(max_length=50, blank=True, null=True)
    
    # Use email as the unique identifier for authentication.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def save(self, *args, **kwargs):
        # Generate a verification token if this is a new user and none exists.
        if not self.pk and not self.email_verification_token:
            self.email_verification_token = self.generate_verification_token()
        print(f"Generated token before saving: {self.email_verification_token}")  # Debug-Ausgabe
        super().save(*args, **kwargs)
        print(f"Token after saving to database: {self.email_verification_token}")  # Debug-Ausgabe

    def generate_verification_token(self):
        # Generate a secure URL-safe token for email verification.
        token = secrets.token_urlsafe(20)
        print(f"Generated token: {token}")  # Debug-Ausgabe
        return token
    
    def generate_password_reset_token(self):
        # Generate a secure token for password reset.
        return secrets.token_urlsafe(20)
    
    def __str__(self):
        return self.email
