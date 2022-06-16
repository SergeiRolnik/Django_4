from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название раздела')
    article_scope = models.ManyToManyField(Article, through='ArticleScope', through_fields=('scope', 'article'))

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name

class ArticleScope(models.Model):
    article = models.ForeignKey(Article, verbose_name='Статья', on_delete=models.CASCADE, related_name='scopes')
    scope = models.ForeignKey(Scope, verbose_name='Раздел', on_delete=models.CASCADE, related_name='tag')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'