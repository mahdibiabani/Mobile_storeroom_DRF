from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
      add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","email", "password1", "password2", "first_name", "last_name"),
            },
        ),
    )
