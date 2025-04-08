from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from products.validators import *


class Products(models.Model):
    """Таблица с продуктом (товаром)"""
    title = models.CharField(max_length=80, blank=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, db_index=True, unique=True, verbose_name='SLUG')
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/', blank=False, validators=[
        image_resolution_validator, image_size_validator
    ], verbose_name='Обложка')

    description = models.TextField( blank=False, verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(blank=True, default=0, validators=[
        MinValueValidator(1),
    ], verbose_name='Цена')

    rating = models.IntegerField(default=1, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], verbose_name='Рейтинг')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    is_active = models.BooleanField(default=False, verbose_name='Публикация')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title', 'price', 'time_create']

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    """Таблица с картинками продукта"""
    prod = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name='Продукт')
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/', blank=False, validators=[
        image_resolution_validator, image_size_validator
        ], verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение к продукту'
        verbose_name_plural = 'Изображения к продукту'

    def __str__(self):
        return f'Изображение к продукту: {self.prod}'


class Category(models.Model):
    """Таблица с категориями"""
    title = models.CharField(max_length=255, unique=True, blank=True, verbose_name='Название')
    slug = models.SlugField(max_length=50, db_index=True, unique=True, verbose_name='SLUG')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


