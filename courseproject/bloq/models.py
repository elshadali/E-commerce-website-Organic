from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='authors')
    description = models.TextField(max_length=2000)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

    class Meta:
        verbose_name = 'Yazar'
        verbose_name_plural = 'Yazarlar'


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'
    

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'


class Bloq(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='bloqs')
    author = models.ForeignKey(
        'bloq.Author',
        on_delete = models.CASCADE,
        related_name = 'bloqs'
    )
    slug = models.SlugField(unique=True)
    category = models.ManyToManyField(
        'bloq.Category',
        related_name = 'bloqs',
    )

    def __str__(self):
        return f'{self.title}'
    

    class Meta:
        verbose_name = 'Bloq'
        verbose_name_plural = 'Bloqlar'
