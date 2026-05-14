from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'email', 'description', 'category']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o último nome'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o telefone'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        if not cleaned_data.get('first_name'):
            self.add_error('first_name', 'O campo first_name é obrigatório.')
        if not cleaned_data.get('last_name'):
            self.add_error('last_name', 'O campo last_name é obrigatório.')
        if not cleaned_data.get('phone'):
            self.add_error('phone', 'O campo phone é obrigatório.')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error('last_name', 'O campo last_name não pode ser igual ao campo first_name.')

            self.add_error('first_name', 'Erro genérico para o campo first_name')
            self.add_error('last_name', 'Erro genérico para o campo last_name')
            self.add_error('phone', 'Erro genérico para o campo phone')
        return super().clean()