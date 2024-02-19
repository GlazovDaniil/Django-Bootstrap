from django.urls import path, re_path
from .views import index, BookListView, BookDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('books/', BookListView.as_view(), name='books-list'),
    re_path(r'^books/(?P<pk>\d+)$', BookDetailView.as_view(), name='books-detail'),
    path('', index, name='index'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
