from django.contrib import admin
from content.models import Content, Category


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'payment_status', 'created_at']
    search_fields = ['title']
    filter_horizontal = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

