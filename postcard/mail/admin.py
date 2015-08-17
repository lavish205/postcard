from django.contrib import admin
from .models import *


@admin.register(Mail)
class UserAdmin(admin.ModelAdmin):
    list_display = ("subject")