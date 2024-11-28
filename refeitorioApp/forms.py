from refeitorioApp.models import Aluno,Evento
from django import forms

class AlunoForms (forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome_aluno','matricula_aluno','foto_aluno']


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'data', 'local', 'descricao', 'foto']
