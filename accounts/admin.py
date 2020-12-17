from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CusomtUserAdmin(UserAdmin):
    fieldsets = (
        (('User info'), {'fields': ('username', 'email', 'first_name', 'last_name', 'introduction')}),)
    list_display = ('username', 'email', 'first_name', 'last_name', 'introduction')


admin.site.register(CustomUser, CusomtUserAdmin)
