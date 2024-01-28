from categories.models import Categories, CategoriesDescription
from django.contrib import admin


class CategoriesInline(admin.TabularInline):
    model = CategoriesDescription


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('categories_image', 'parent_id', 'sort_order', 'date_added', 'last_modified', 'categories_status')
    fields = ['categories_image', 'parent_id', 'sort_order', 'categories_status']
    inlines = [
        CategoriesInline,
    ]


@admin.register(CategoriesDescription)
class CategoriesDescriptionAdmin(admin.ModelAdmin):
    list_display = ('categories_name',)
    fields = ['categories', 'language_id', 'categories_name', 'categories_heading_title', 'categories_description',
              'categories_meta_title', 'categories_meta_description', 'categories_meta_keywords',
              'categories_seo_url']
