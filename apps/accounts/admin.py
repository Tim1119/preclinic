from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, SignUpForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = SignUpForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "pkid",
        "id",
        "email",
        "full_name",
        "is_superuser",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["id", "email"]
    list_filter = [
        "email",
        "full_name",
        "is_patient",
        "is_employee",
        "is_staff",
        "is_active",
    ]
    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "full_name",
                    "has_updated_profile",

                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_patient",
                    "is_employee",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("full_name", "email","is_patient","is_employee", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ["email", "full_name"]


admin.site.register(User, UserAdmin)
