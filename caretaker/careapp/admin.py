from django.contrib import admin

from .models import Category

admin.site.register(Category)


class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
