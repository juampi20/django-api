from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    fields = ("name", "alias")
    list_display = ("alias", "name")
    list_display_links = ("alias",)
    search_fields = ["name", "alias"]