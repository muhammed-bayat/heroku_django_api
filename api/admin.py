from django.contrib import admin
from .models import Article, Material, Experiment, Category
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Experiment)