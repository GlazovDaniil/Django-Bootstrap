from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, BookInstance, Author


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


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 6


class BookDetailView(DetailView):
    model = Book


class AuthorView(ListView):
    model = Author
    paginate_by = 6


class AuthorDetailView(DetailView):
    model = Author


def about(request):
    text_head = 'Сведения о компании'
    name = 'ООО "ГлаДИ"'
    rab1 = ('Разработка приложений на основе '
            'систем искусственного интеллекта')
    rab2 = 'Распознавание объектов дорожной инфраструктуры'
    rab3 = ('Создание графических АРТ-объектов на основе '
            'систем искусственного интелпекта')
    rab4 = ('Создание цифровых интерактивных книг, учебных пособий'
            ' автоматизированных обучающих систем')
    context = {'text_head': text_head, 'name': name, 'rab1': rab1, 'rab2': rab2, 'rab3': rab3, 'rab4': rab4}
    return render(request, 'books/about.html', context)


def contact(request):
    text_head = 'Контакты'
    name = 'ООО "ГлаДИ"'
    address = 'Москва, ул. Планерная, д. 20, к. 1'
    tel = '495-345-45-45'
    email = 'iis_info@mail.ru'
    context = {'text_head': text_head, 'name': name, 'address': address, 'tel': tel, 'email': email}
    return render(request, 'books/contact.html', context)
