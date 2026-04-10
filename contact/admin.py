from django.contrib import admin
from .models import Contact, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'id','first_name', 'last_name', 'phone', 'email', 'created_date','show')
    ordering = ('-id',)
    search_fields = ('id', 'first_name', 'last_name', 'email')
    list_filter = ('created_date',)
    list_editable = ('first_name', 'last_name', 'phone', 'email', 'show') 
    list_per_page = 20
    list_max_show_all = 100
