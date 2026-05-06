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

    first_name = models.CharField(max_length=50, verbose_name='Primeiro Nome') # verbose_name para exibir um nome mais amigável no admin
    last_name = models.CharField(max_length=50, verbose_name='Último Nome')
    phone = models.CharField(max_length=15, verbose_name='Telefone')
    email = models.EmailField(max_length=254, blank=True, verbose_name='E-mail') # o blank=True permite que o campo seja opcional
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Data de Criação')
    description = models.TextField(blank=True, verbose_name='Descrição')

    show = models.BooleanField(default=True, verbose_name='Mostrar') # Campo para controlar a visibilidade do contato
    picture = models.ImageField(upload_to='contact_pictures/%Y/%m/%d/', blank=True, null=True, verbose_name='Foto') # Campo para armazenar a foto do contato
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Categoria') # Relacionamento com a categoria

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # Relacionamento com o usuário proprietário do contato

    def __str__(self):
        return f"ID({self.id}) - {self.first_name} {self.last_name}"
