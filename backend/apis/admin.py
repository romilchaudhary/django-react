from django.contrib import admin
from .models import Group

# Register your models here.
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'description', 'created')
    list_display = ('id', 'name', 'location', 'description', 'created')
    empty_value_display = '-empty-'
