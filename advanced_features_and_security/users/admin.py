from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """Customize the admin panel for the custom user model."""
    
    model = CustomUser

    # Fields to display in the admin list view
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')

    # Fields to filter by in the admin panel
    list_filter = ('is_staff', 'is_active')

    # Define the fieldsets (for viewing/editing users)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    # Define fields to be used when creating a user in the admin panel
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active'),
        }),
    )

    # Fields to search for in the admin panel
    search_fields = ('email', 'username')
    ordering = ('email',)

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(CustomUser, CustomUserAdmin)
