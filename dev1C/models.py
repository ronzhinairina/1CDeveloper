from django.db import models

TYPES = (
    ('text', 'Текст'),
    ('image', 'Изображения'),
    ('table', 'Таблица')
)

PAGES = (
    ('home', 'Главная'),
    ('demand', 'Востребованность'),
    ('areas', 'География'),
    ('skills', 'Навыки'),
    ('vacancies', 'Последние вакансии')
)


class Content(models.Model):
    title = models.CharField(max_length=63, blank=True)
    image = models.ImageField(blank=True)
    content = models.TextField(blank=True)
    style = models.TextField(blank=True)
    type = models.CharField(max_length=25, choices=TYPES)
    block = models.ForeignKey('Block', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.block.title}. {self.type}'


class Block(models.Model):
    title = models.CharField(max_length=63)
    page = models.CharField(max_length=25, choices=PAGES)
    style = models.TextField(blank=True)

    def __str__(self):
        return self.title


# Create your models here.
