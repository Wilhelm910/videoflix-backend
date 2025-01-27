import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from users_app.models import CustomUser
from rest_framework.authtoken.models import Token

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user(db):
    user = CustomUser.objects.create_user(
        email="testuser@example.com",
        password="securepassword123",
        is_verified=True
    )
    return user

@pytest.fixture
def unverified_user(db):
    user = CustomUser.objects.create_user(
        email="unverified@example.com",
        password="securepassword123",
        is_verified=False
    )
    return user

@pytest.fixture
def auth_token(test_user):
    token, _ = Token.objects.get_or_create(user=test_user)
    return token.key

### Test für RegisterUserView
@pytest.mark.django_db
def test_register_user(api_client):
    url = reverse("register")  # Hier den richtigen URL-Namen verwenden
    data = {
        "email": "newuser@example.com",
        "password": "password123"
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert CustomUser.objects.filter(email="newuser@example.com").exists()

### Test für VerifyEmailView
def test_verify_email(api_client, test_user):
    # Setze den Benutzer auf unbestätigt
    test_user.is_verified = False
    test_user.save()

    # Erstelle und speichere den Token
    test_user.email_verification_token = "testtoken"
    test_user.save()

    url = reverse("verify-email", args=["testtoken"])
    response = api_client.get(url)

    # Überprüfe die Antwort und ob der Benutzer verifiziert wird
    test_user.refresh_from_db()
    assert response.status_code == 200
    assert test_user.is_verified
    
@pytest.mark.django_db
def test_verify_email_invalid_token(api_client):
    url = reverse("verify-email", args=["invalidtoken"])  # Korrekte URL für den Token
    response = api_client.get(url)
    assert response.status_code == 404

### Test für UserLoginView
def test_user_login(api_client, test_user):
    url = reverse("login")
    data = {
        "email": "testuser@example.com",
        "password": "securepassword123"
    }
    response = api_client.post(url, data)
    assert response.status_code == 200
    assert "token" in response.data

def test_user_login_unverified(api_client, unverified_user):
    url = reverse("login")
    data = {
        "email": "unverified@example.com",
        "password": "securepassword123"
    }
    response = api_client.post(url, data)
    assert response.status_code == 403
    assert response.data["error"] == "User is not verified. Please verify your email."

### Test für LogoutView
def test_logout(api_client, test_user, auth_token):
    url = reverse("logout")
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {auth_token}")
    response = api_client.post(url)
    assert response.status_code == 200
    assert not Token.objects.filter(user=test_user).exists()

### Test für CurrentUserView
def test_get_current_user(api_client, test_user, auth_token):
    url = reverse("current-user")
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {auth_token}")
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data["email"] == "testuser@example.com"

# ### Test für ChangePasswordView
# def test_change_password(api_client, test_user, auth_token):
#     url = reverse("change-password")
#     api_client.credentials(HTTP_AUTHORIZATION=f"Token {auth_token}")

#     # Achte darauf, dass das neue Passwort korrekt übergeben wird
#     data = {
#         "new_password": "newsecurepassword123"
#     }

#     response = api_client.post(url, data)

#     # Überprüfe, ob der Statuscode 200 ist und das Passwort geändert wurde
#     assert response.status_code == 200
#     test_user.refresh_from_db()
#     assert test_user.check_password("newsecurepassword123")

### Test für PasswordResetView
def test_password_reset(api_client, test_user):
    url = reverse("password-reset")
    data = {"email": "testuser@example.com"}
    response = api_client.post(url, data)
    assert response.status_code == 200
    test_user.refresh_from_db()
    assert test_user.password_reset_token is not None

### Test für PasswordResetConfirmView
def test_password_reset_confirm(api_client, test_user):
    test_user.password_reset_token = "reset-token"
    test_user.save()
    url = reverse("password_reset_confirm")  # Korrekte URL für den Reset
    data = {
        "token": "reset-token",
        "new_password": "newsecurepassword123"
    }
    response = api_client.post(url, data)
    assert response.status_code == 200
    test_user.refresh_from_db()
    assert test_user.check_password("newsecurepassword123")
