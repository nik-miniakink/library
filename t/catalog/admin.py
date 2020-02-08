from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Genre)


class BooksInline(admin.TabularInline):  # Описываем вставляеемую часть Book вертикально
    model = Book
    extra = 0


class BookInstanceInline(admin.TabularInline):  # Описываем вставляемую часть горизонтально
    model = BookInstance
    extra = 0


@admin.register(BookInstance)  # регистрация модели
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'status', 'due_back', 'book_id', 'add_1', 'modern_1')  # Отображаемые поля
    list_filter = ('status', 'due_back')  # Отображаемые фильтры

    fieldsets = (  # Разделение отображения на 2 секции
        (None, {
            'fields': ('book_name', 'imprint', 'book_id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author', 'display_genre', 'language', 'image', 'add', 'modern')
    inlines = [BookInstanceInline]  # Вставляем описанное выше как список


@admin.register(Author)  # регистрация модели Автор
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death','gender', 'image')  # Отображение полей в общей таблице
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death'), 'summary_author', 'gender', 'image']  # Отображение полей в странице автора. Списком- горизонтально отображается
    inlines = [BooksInline]  # Вставляем описанное выше как список
