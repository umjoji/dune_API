from django.contrib import admin
from .models import (
    Author,
    Book,
    Comic,
    Director,
    Illustrator,
    Quote,
    Movie,
    Series,
    ShortStories,
)


# class BookInstanceInline(admin.TabularInline):
# model = BookInstance

# class AuthorInline(admin.TabularInline):
#     model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    fields = ['first_name', 'last_name']
    # inlines = [AuthorInline]


# @admin.register(Book)  # register the book model to be managed by Django Admin site
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'year')


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register your models here.
# admin.site.register(BookInstance)
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Illustrator)
admin.site.register(Director)
admin.site.register(Quote)
admin.site.register(Comic)
admin.site.register(Movie)
admin.site.register(Series)
admin.site.register(ShortStories)
admin.site.register(Book)
