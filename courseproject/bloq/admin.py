from django.contrib import admin
from .models import Author, Category, Bloq

admin.site.register(Author)



@admin.register(Bloq)
class BloqAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'author']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

