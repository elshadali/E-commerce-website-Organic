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


class Message(models.Model):
    full_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True, null=True)
    subject = models.CharField(max_length=200, null=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.full_name}, {self.subject}'
    
    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'message'


