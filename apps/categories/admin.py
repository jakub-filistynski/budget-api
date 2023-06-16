from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ("budget", "finance_type")
    list_display = ("name", "finance_type", "budget")
    search_fields = ("name",)
