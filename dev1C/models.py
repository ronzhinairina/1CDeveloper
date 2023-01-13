from django.db import models

TYPES = (
    ('text', 'Текст'),
    ('image', 'Изображения'),
    ('table', 'Таблица'),
    ('list', 'Список')
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
    image = models.ImageField(upload_to='images/', blank=True)
    content = models.TextField(blank=True)
    style = models.TextField(blank=True)
    type = models.CharField(max_length=25, choices=TYPES)
    block = models.ForeignKey('Block', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.block.title}. {self.type}'

    class Meta:
        verbose_name = 'Содержание блока'
        verbose_name_plural = "Содержания блока"


class Block(models.Model):
    title = models.CharField(max_length=63, blank=True)
    title_style = models.TextField(blank=True,null= True)
    page = models.CharField(max_length=25, choices=PAGES)
    style = models.TextField(blank=True)

    def __str__(self):
        if self.title == "":
            return f'{self.page}.Блок'
        return self.title

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = "Блоки"


# Create your models here.
