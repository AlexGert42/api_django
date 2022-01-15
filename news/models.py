from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(max_length=1000, blank=True, verbose_name='текст')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='фото')
    time_create = models.TimeField(auto_now_add=True, verbose_name='дата создания')
    time_update = models.TimeField(auto_now=True, verbose_name='дата изминения')
    is_published = models.BooleanField(default=True, verbose_name='публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'
        ordering = ['-time_update', 'pk']



class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='заголовок')
    slug = models.SlugField(max_length=150, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Categorys'
        verbose_name_plural = 'Categorys'
        ordering = ['pk']

