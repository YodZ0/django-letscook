from django.contrib import admin
from .models import UserCart


@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    filter_horizontal = ['recipies']
