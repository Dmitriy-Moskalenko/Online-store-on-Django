from django.contrib import admin

from products.models import Products, ProductImages, Category


class ProductImagesAdminInline(admin.TabularInline):
    model = ProductImages
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'image', 'description', 'category',
              'price', 'user', 'is_active']
    list_display = ['id', 'title', 'category']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImagesAdminInline]


class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'slug']
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Products, ProductAdmin)
admin.site.register(Category, CategoryAdmin)