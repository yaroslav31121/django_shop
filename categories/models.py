from django.db import models


class Categories(models.Model):
    categories_image = models.CharField(max_length=255)
    parent_id = models.IntegerField()
    sort_order = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    categories_status = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.categories_image


class CategoriesDescription(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    language_id = models.PositiveSmallIntegerField()
    categories_name = models.CharField(max_length=255)
    categories_heading_title = models.CharField(max_length=255)
    categories_description = models.TextField()
    categories_meta_title = models.CharField(max_length=255)
    categories_meta_description = models.TextField()
    categories_meta_keywords = models.CharField(max_length=255)
    categories_seo_url = models.CharField(max_length=255)

    def __str__(self):
        return self.categories
