from django.contrib import admin
from .models import Author, Book, Category

# Register the models
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
