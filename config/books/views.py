from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, BookInstance, Author

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'

def index(request):
    text_head = 'На данном сайте можно пролучить книги в электронном виде'
    # Данные о книгах и их количестве
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    # Данные об экземплярах книг в БД
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'На складе')
    num_instances_available = BookInstance.objects.filter(status__exact=1).count()
    # Данные об авторах книг
    authors = Author.objects
    num_authors = Author.objects.all().count()
    context = {'text_head': text_head,
               'books': books,
               'num_books': num_books,
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'authors': authors,
               'num_authors': num_authors,}
    return render(request, 'books/index.html', context)