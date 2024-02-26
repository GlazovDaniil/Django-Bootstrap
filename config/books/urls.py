from django.urls import path, re_path
from .views import index, BookListView, BookDetailView, AuthorView, AuthorDetailView, about, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('books/', BookListView.as_view(), name='books-list'),
    re_path(r'^books/(?P<pk>\d+)$', BookDetailView.as_view(), name='books-detail'),
    path('', index, name='index'),
    path('authors/', AuthorView.as_view(), name='authors-list'),
    re_path(r'^authors/(?P<pk>\d+)$', AuthorDetailView.as_view(), name='authors-detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
