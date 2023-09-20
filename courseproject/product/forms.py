from django import forms
from django.utils.translation import gettext_lazy as _
from .models import ProductReview


class ReviewForm(forms.ModelForm):

    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': _('Mətn'),
        'rows': '5',
        'cols': '30',
    }))

    class Meta:
        model = ProductReview
        fields = ['text']