from django.shortcuts import render
from .models import *
from django.views import generic
# Create your views here.


def index(request):
    # Генерация количеств элементов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count
    #  Наличие доступных книг
    num_instances_available = BookInstance.objects.filter(status='a').count
    num_authors = Author.objects.count()
    num_genre = Genre.objects.count()
    book_hoi = Author.objects.filter(first_name='Юваль').count

    return render(request, 'index.html', context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'book_hoi': book_hoi,

    }
                  )


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.filter(book_name__icontains='')[:5]

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(BookListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['some_data'] = 'This is just some data'
        return context


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Author.objects.filter()[:5]

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(AuthorListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['some_data'] = 'This is just some data'
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'

