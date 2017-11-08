from django.contrib import admin
from .models import Owner

class OwnerAdmin(admin.ModelAdmin):
    list_display = ['username']
    search_fields = []

admin.site.register(Owner, OwnerAdmin)