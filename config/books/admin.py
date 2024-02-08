from django.contrib import admin
from .models import Book, Author, BookInstance, Publisher, Language, Genre, Status
from django.utils.html import format_html


@admin.register(Author)  # используем декоратаор, то же самое что и admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'photo', 'show_photo')
    fields = ['first_name', 'last_name', ('date_of_birth', 'photo')]
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    show_photo.short_description = 'Фото'


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author', 'show_photo')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline, ]
    readonly_fields = ["show_photo"]

    def show_photo(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-height: 100px;">')

    show_photo.short_description = 'Обложка'


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'inv_nom')}),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back')}),
    )



admin.site.register(Publisher)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Status)

'''
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Author)  # используем декоратаор, то же самое что и admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['name', 'last_name',
              ('date_of_birth', 'date_of_death')]


@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'autor')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back', 'borrower')}),
    )
'''