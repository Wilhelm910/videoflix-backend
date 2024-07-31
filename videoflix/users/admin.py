# from django.contrib import admin

# from users.models import CustomUser

# # Register your models here.
# admin.site.register(CustomUser)

from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_verified', 'email_verification_token', 'is_staff', 'is_superuser')
    search_fields = ('email',)
