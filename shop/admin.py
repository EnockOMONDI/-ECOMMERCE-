from django.contrib import admin
from .models import Category, Product, SubCategory, MiniCategory





class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)



class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(SubCategory, SubCategoryAdmin)


class MiniCategoryAdmin(admin.ModelAdmin):
    list_display = ['category','subcategory', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(MiniCategory, MiniCategoryAdmin)

