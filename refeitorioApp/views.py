from django.shortcuts import render, get_object_or_404, redirect
from refeitorioApp.forms import AlunoForms
from refeitorioApp.models import Aluno
from .models import Evento
from .forms import EventoForm 

# Página inicial para o cadastro de alunos
def home(request):
    form = AlunoForms()
    context = {'form': form}
    return render(request, 'refeitorio/home.html', context)

# Função para criar um novo aluno
def new_aluno(request):
    alunos = Aluno.objects.all()  # Pegando todos os alunos cadastrados
    form = AlunoForms(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            aluno = form.save()  # Salvando o novo aluno
            aluno.save()
            form = AlunoForms()  # Reseta o formulário após o envio
    context = {'form': form, 'alunos': alunos}
    return render(request, 'refeitorio/new_aluno.html', context)

# Função para editar um aluno existente
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)  # Busca aluno pelo id
    form = AlunoForms(instance=aluno)
    if request.method == 'POST':
        form = AlunoForms(request.POST, request.FILES, instance=aluno)
        if form.is_valid():
            form.save()  # Salva as alterações no aluno
            return redirect('new_aluno')  # Redireciona para a página de novo aluno
    context = {'form': form, 'aluno': aluno}
    return render(request, 'refeitorio/editar_aluno.html', context)

# Função para excluir um aluno
def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    if request.method == "POST":
        aluno.delete()  # Exclui o aluno
        return redirect("new_aluno")  # Redireciona para a página de novo aluno
    return render(request, "refeitorio/excluir_aluno.html", {"aluno": aluno})

# Função para criar um novo evento
def new_evento(request):
    eventos = Evento.objects.all()  # Pegando todos os eventos cadastrados
    form = EventoForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            evento = form.save()  # Salvando o novo evento
            evento.save()
            return redirect('evento')  # Redireciona para a página de eventos
    context = {'form': form, 'eventos': eventos}
    return render(request, 'refeitorio/new_evento.html', context)

# Função para listar todos os eventos
def mostrar_evento(request):
    eventos = Evento.objects.all()  # Pegando todos os eventos cadastrados
    context = {'eventos': eventos}
    return render(request, 'refeitorio/show_evento.html', context)

# Função para editar um evento existente
class EventoForm:
    pass


def editar_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)  # Busca o evento pelo id
    form = EventoForm(instance=evento)
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()  # Salva as alterações no evento
            return redirect('new_evento')  # Redireciona para a página de novo evento
    context = {'form': form, 'evento': evento}
    return render(request, 'refeitorio/editar_evento.html', context)

# Função para excluir um evento
def excluir_evento(request, id):
    evento = get_object_or_404(Evento, pk=id)  # Corrigido: deve buscar Evento e não Aluno
    if request.method == "POST":
        evento.delete()  # Exclui o evento
        return redirect("new_evento")  # Redireciona para a página de novo evento
    return render(request, "refeitorio/excluir_evento.html", {"evento": evento})

# Função para listar os eventos
def evento(request):
    eventos = Evento.objects.all()  # Pegando todos os eventos cadastrados
    context = {'eventos': eventos}
    return render(request, 'refeitorio/evento.html', context)