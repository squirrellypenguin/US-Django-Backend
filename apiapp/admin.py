from django.contrib import admin

# Register your models here.
from .models import Event

class EventAdmin(admin.ModelAdmin):

    list_display = ("title", 'summary', 'user_id')

admin.site.register(Event, EventAdmin)