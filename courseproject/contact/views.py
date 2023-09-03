from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from .models import Contact
from django.contrib import messages

def contact_list(request):

    contacts= Contact.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Müraciətiniz uğurla qeydə alındı, tezliklə sizinlə əlaqə saxlanılacaq')
            return redirect(reverse("contact"))

    context = {
        'contacts': contacts,
        'form' : form,
    }
    return render(request, 'contact/contact.html', context)