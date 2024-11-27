from django.contrib import admin
from storeroom.models import Mobile

class MobileAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'color', 'status']


admin.site.register(Mobile, MobileAdmin)