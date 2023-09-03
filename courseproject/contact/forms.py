from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact


class ContactForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Ad, soyad')
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': _('E-mail')
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': _('Başlıq')
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': _('Mətn'),
        'rows': '6'
    }))

    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']