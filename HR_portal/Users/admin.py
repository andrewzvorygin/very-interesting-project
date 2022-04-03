from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, HeadDepartment


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("last_name", "first_name", "patronymic", "email", "photo")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    change_password_form = AdminPasswordChangeForm
    list_display = ['id', 'email', 'username', 'last_name', 'first_name', 'patronymic', 'is_staff', 'is_active']
    list_filter = ('email', 'is_staff', 'is_active',)


admin.site.register(CustomUser, CustomUserAdmin)


class HeadDepartmentAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['user', 'department']


admin.site.register(HeadDepartment, HeadDepartmentAdmin)
