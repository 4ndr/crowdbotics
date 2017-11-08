from django.contrib import admin
from .models import Dog, Cat

class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthday']
    search_fields = ['name']

admin.site.register(Dog, PetAdmin)
admin.site.register(Cat, PetAdmin)