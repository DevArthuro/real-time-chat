from django.contrib import admin
from .models import ProfileModel
# Register your models here.
@admin.register(ProfileModel)
class RegisterFriends(admin.ModelAdmin):
    list_display = ['slug', 'name', 'user']

