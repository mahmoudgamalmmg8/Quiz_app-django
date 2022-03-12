from django.contrib import admin
from .models import CustomUserStudent
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    model = CustomUserStudent
    add_form = CustomUserCreationForm
admin.site.register(CustomUserStudent,CustomUserAdmin)
