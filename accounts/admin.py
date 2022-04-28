from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Application

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    readonly_fields = ('id',)
    list_display = ['username', 'email',]

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
	readonly_fields = ('id',)
	list_display = ['name']

admin.site.register(CustomUser, CustomUserAdmin)