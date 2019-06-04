from django.contrib import admin

from .models import (
    cabeleireiro,
    cliente
)


@admin.register(cabeleireiro)
class CabelereiroAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['nome', 'email']
    search_fields = ['nome', 'email']


@admin.register(cliente)
class ClientAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['nome', 'email']
    search_fields = ['nome', 'email']