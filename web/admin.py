from django.contrib import admin

from .models import *
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin
from django.contrib.auth.models import User


admin.site.unregister(User)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['alias', 'name']
    ordering = ['alias']


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


@admin.register(User)
class UserAdmin(OriginalUserAdmin):
    inlines = [ProfileInline]
