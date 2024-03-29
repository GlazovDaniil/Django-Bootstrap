# Generated by Django 3.1.14 on 2024-02-08 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя автора', max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Введите фамилию автора', max_length=100, verbose_name='Фамилия автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Введите дату рождения', null=True, verbose_name='Дата рождения')),
                ('about', models.TextField(help_text='Введите сведенья об авторе', verbose_name='Сведенья об авторе')),
                ('photo', models.ImageField(blank=True, help_text='Введите дату рождения', null=True, upload_to='images', verbose_name='Дата рождения')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр книги', max_length=200, verbose_name='Жанр книги')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите язык книги', max_length=20, verbose_name='Язык книги')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название издательства', max_length=20, verbose_name='Название издательства')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите статус экземпляра книги', max_length=20, verbose_name='Статус экземпляра книги')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(help_text='Введите изображение обложки', null=True, upload_to='images', verbose_name='Изображение обложки'),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Введите цену книги', max_digits=7, null=True, verbose_name='Цена (руб.)'),
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Введите крадкое описание книги', max_length=1000, null=True, verbose_name='Крадкое описание книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.CharField(help_text='Введите год издания', max_length=4, null=True, verbose_name='Год издания'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='Должно содержать 13 символов', max_length=13, verbose_name='ISBN книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='Введите название книги', max_length=200, verbose_name='Название книги'),
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text='Введите инвентарный номер книги', max_length=20, null=True, verbose_name='Инвентарный номер')),
                ('due_back', models.DateField(blank=True, help_text='Введите конец срока статуса', null=True, verbose_name='Дата окончания статуса')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('status', models.ForeignKey(help_text='Изменить состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='books.status', verbose_name='Состояние экземпляра книги')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Выберите жанр книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='books.genre', verbose_name='Жанр книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Выберите язык книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='books.language', verbose_name='Язык книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(help_text='Выберите издатльство', null=True, on_delete=django.db.models.deletion.CASCADE, to='books.publisher', verbose_name='Издатльство'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выберите автора(ов) книги', to='books.Author', verbose_name='Автор(ы) книги'),
        ),
    ]
