from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Bundle, BundleDetail, CUser, Inventory, Item

# Register your models here.
admin.site.register(CUser, UserAdmin)
admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(Bundle)
admin.site.register(BundleDetail)