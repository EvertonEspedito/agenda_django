from django.shortcuts import render
from contact.forms import ContactForm


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