from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CUser, Item

# Register your models here.
admin.site.register(CUser, UserAdmin)
admin.site.register(Item)