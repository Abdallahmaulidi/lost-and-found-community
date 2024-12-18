from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'posted_by', 'date_posted', 'location')
    list_filter = ('status', 'date_posted')
    search_fields = ('title', 'description', 'location')
    readonly_fields = ('date_posted',)
    date_hierarchy = 'date_posted'