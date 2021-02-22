from django.contrib import admin

from apps.userapp import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'position', 'level')
