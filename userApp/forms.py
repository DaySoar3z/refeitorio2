from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User


class UsuarioForm(UserCreationForm):
    FIRST_NAME_CHOICES = [
        ('Aluno', "Aluno"),
        ('Servidor', "Servidor"),
        ('Chefe', "Chefe")
    ]

    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name']

    username = forms.CharField(label='Matricula: ')
    email = forms.EmailField(label='E-mail: ')
    last_name = forms.CharField(label='Nome completo: ')
    first_name = forms.ChoiceField(
        label='Status: ',
        choices=FIRST_NAME_CHOICES,
        widget=forms.Select(attrs={'class0': 'custom=select'}),
        initial='Aluno'
    )
