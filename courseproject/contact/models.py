from django.db import models

class Contact(models.Model):
    phone = models.CharField('Telefon', max_length=50)
    address = models.TextField('Unvan', max_length=2000)
    mail = models.TextField('Elektron pocht', max_length=2000)
    open = models.TextField('Ish rejimi', max_length=2000)
    

    def __str__(self):
        return self.phone
    
    class Meta:
        verbose_name = 'Elaqe'
        verbose_name_plural = 'Elaqe'

