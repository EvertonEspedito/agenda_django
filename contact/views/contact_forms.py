from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from contact.models import Contact
from django.db.models import Q

from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone']

    def clean(self):
        cleaned_data = super().clean()
        self.add_error('first_name', 'O campo first_name é obrigatório.')
        self.add_error('last_name', 'O campo last_name é obrigatório.')
        self.add_error('phone', 'O campo phone é obrigatório.')
        
        return cleaned_data

def create(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or do something after successful form submission
    else:
        form = ContactForm()

    context = {
       'form': ContactForm()
    }
    return render(request, 'contact/create.html', context)