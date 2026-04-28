from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from contact.models import Contact
from django.db.models import Q


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')


    paginator = Paginator(contacts, 10)  
    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)  

    context = {
        'contacts': contacts,
        'site_title': 'Contatos'
    }
    return render(
        request, 
        'contact/index.html',
        context
    )

def sobre(request):
    context = {'site_title': 'Sobre'}
    return render(request, 'sobre/about.html', context)

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    contact_name = f'{single_contact.first_name} {single_contact.last_name}'
    context = {
        'contact': single_contact,
        'site_title': contact_name
    }
    return render(
        request, 
        'contact/contact.html',
        context
    )

def search(request):
    search_term = request.GET.get('q', '').strip()
    # Correto: Filtros primeiro, fatiamento por último
    contacts = Contact.objects.filter(
        Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term)
          | Q(phone__icontains=search_term) | Q(email__icontains=search_term),
        show=True
    ).order_by('-id')
        
    paginator = Paginator(contacts, 10)  
    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number) 

    context = {
        'contacts': contacts,
        'site_title': f'Pesquisar por "{search_term}"'
    }
    return render(
        request, 
        'contact/index.html',
        context
    )
