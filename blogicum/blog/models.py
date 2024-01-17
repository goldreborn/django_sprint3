# cinema/models.py
# Импортируем модуль с классом Model, от которого будем наследовать модели:
from django.db import models
from blog.abstractmodel import AbstractModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(AbstractModel):

    title = models.CharField(
        max_length=256,
        verbose_name='Заголовок'
    )

    description = models.TextField(
        verbose_name='Описание')

    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='''Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'''
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(AbstractModel):

    name = models.CharField(
        max_length=256,
        verbose_name='Название места'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(AbstractModel):

    title = models.CharField(
        max_length=256,
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
        verbose_name='Автор публикации'
    )

    location = models.ForeignKey(
        Location,
        verbose_name='Местоположение',
        on_delete=models.SET_NULL,
        null=True,
    )

    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
