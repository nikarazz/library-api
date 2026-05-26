from django.db import models
from django.conf import settings


class Author(models.Model):
    """Модель автора книги"""
    name = models.CharField(max_length=255, verbose_name="Имя")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    bio = models.TextField(blank=True, verbose_name="Биография")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Genre(models.Model):
    """Модель жанра книги"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Book(models.Model):
    """Модель книги"""
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    published_date = models.DateField(null=True, blank=True, verbose_name="Дата публикации")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name="Автор")
    genres = models.ManyToManyField(Genre, related_name='books', blank=True, verbose_name="Жанры")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Comment(models.Model):
    """Модель комментария к книге"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', verbose_name="Книга")
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='comments',
        verbose_name="Пользователь"
    )

    def __str__(self):
        return f"Комментарий к '{self.book.title}'"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"