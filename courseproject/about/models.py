from django.db import models

class About(models.Model):
    title = models.CharField('Haqqimizda', max_length=50)
    description = models.TextField('Haqqimizda')
    image = models.ImageField(upload_to='about')


    def __str__(self):
        return f'{self.title}'
    

    class Meta:
        verbose_name = 'Haqqimizda'
        verbose_name_plural = 'Haqqimizda'


class SocialMedia(models.Model):
    instagram = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    facebook = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    youtube = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    tiktok = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    linkedin = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Sosial media'
        verbose_name_plural = 'Sosial media'