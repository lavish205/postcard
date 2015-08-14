from django.contrib import admin
from django.contrib.admin.util import flatten_fieldsets

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "joined_on")
    list_filter = ("joined_on",)
    # readonly_fields = ("full_name", "email", "joined_on")

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

