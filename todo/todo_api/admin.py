from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import CustomUser, Todo

from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)  # dont forget to add this line
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # for creation
    form = CustomUserChangeForm  # for editing
    model = CustomUser  # choosing the model
    list_display = ["email", "username", "phone_number", "is_staff"]

    ## adding field set for users
    fieldsets = UserAdmin.fieldsets + (
        (
            "contact number",
            {"fields": ("phone_number",)},
        ),  # dont forget to make this as tuple
    )


@admin.register(Todo)
class AdminTodo(admin.ModelAdmin):

    list_display = ["task", "timestamp", "completed", "updated", "user"]
