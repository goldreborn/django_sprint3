from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

MAX_CHAR_LENGTH = 256


class AbstractModel(models.Model):

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True


class Category(AbstractModel):

    title = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        verbose_name='Заголовок'
    )

    description = models.TextField(
        verbose_name='Описание')

    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(AbstractModel):

    name = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        verbose_name='Название места'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(AbstractModel):

    title = models.CharField(
        max_length=MAX_CHAR_LENGTH,
        verbose_name='Заголовок'
    )

    text = models.TextField(
        verbose_name='Текст')

    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем '
                  '— можно делать отложенные публикации.')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации'
    )

    location = models.ForeignKey(
        Location,
        verbose_name='Местоположение',
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True,
    )

    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        related_name='posts',
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['id']
