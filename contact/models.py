from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories' # Define o nome plural para a categoria no admin

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contacts' # Define o nome plural para o contato no admin

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True) # o blank=True permite que o campo seja opcional
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True) 
    
    show = models.BooleanField(default=True) # Campo para controlar a visibilidade do contato
    picture = models.ImageField(upload_to='contact_pictures/%Y/%m/%d/', blank=True, null=True) # Campo para armazenar a foto do contato
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) # Relacionamento com a categoria

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # Relacionamento com o usuário proprietário do contato

    def __str__(self):
        return f"ID({self.id}) - {self.first_name} {self.last_name}"
