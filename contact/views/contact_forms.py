from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from contact.models import Contact
from django.db.models import Q

def create(request):

    context = {
     
    }
    return render(request, 'contact/create.html', context)