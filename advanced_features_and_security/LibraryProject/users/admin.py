from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """Custom admin configuration for the CustomUser model."""

    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("email",)

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("username", "email", "password1", "password2", "date_of_birth", "profile_photo")}),
    )

# Register the CustomUser model with the custom admin
admin.site.register(CustomUser, CustomUserAdmin)
