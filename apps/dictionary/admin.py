from django.contrib import admin

from apps.dictionary import models


@admin.register(models.Level)
class LevelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Framework)
class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')
