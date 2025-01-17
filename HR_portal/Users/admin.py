from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['id', 'email', 'username', 'last_name', 'first_name', 'patronymic', 'is_staff', 'is_active']
    list_filter = ('email', 'is_staff', 'is_active',)


admin.site.register(CustomUser, CustomUserAdmin)
