from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('phone', 'is_staff', 'is_superuser')
    list_filter = ('phone', )

    fieldsets = (
        (
            'Main', {
                'fields': ('phone', 'password',)
            }
        ),
        (
            'Additional information', {
                'fields': ('first_name', 'last_name', 'avatar',)
            }
        ),
        (
            'Permissions', {
                'fields': ('is_staff', 'is_active', 'groups',)
            }
        )
    )
    add_fieldsets = (
        (
            'Main', {
                'classes': ('wide',),
                'fields': ('phone', 'password1', 'password2',)
            }
        ), (
            'permissions', {
                'fields': ('is_staff', 'is_active', 'groups',)
            }
        )
    )
    search_fields = ('phone',)
    ordering = ('phone',)