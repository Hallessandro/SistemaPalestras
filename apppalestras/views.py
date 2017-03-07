from django.contrib.auth.management import get_default_username
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.forms import formset_factory
import datetime as DT
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.forms import SetPasswordForm

from apppalestras.forms import *
from apppalestras.models import *


def home(request):
    return render(request, 'base.html')

def palestrante_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        palestrantes = Palestrante.objects.filter(nome__contains=criterio).order_by('nome')
    else:
        palestrantes = Palestrante.objects.all().order_by('nome')
        criterio =""
    paginator =Paginator(palestrantes,10)
    page = request.GET.get('page')
    try:
        palestrantes = paginator.page(page)
    except PageNotAnInteger:
        palestrantes=paginator.page(1)
    except EmptyPage:
        palestrantes = paginator.page(paginator.num_pages)
    dados={'palestrantes':palestrantes,'criterio':criterio,'paginator':paginator,'page_obj':palestrantes}
    return render(request, 'Palestrante/palestrante_list.html',dados)

def palestrante_new(request):
    if (request.method=="POST"):
        form=PalestranteForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('palestrante_list')
    else:
        form=PalestranteForm()
    dados={'form':form}
    return render(request,'Palestrante/palestrante_form.html',dados)

def palestrante_update(request,pk):
    palestrante=Palestrante.objects.get(id=pk)
    if (request.method=="POST"):
        form=PalestranteForm(request.POST,instance=palestrante)
        if(form.is_valid()):
            form.save()
            return redirect('palestrante_list')
    else:
        form=PalestranteForm(instance=palestrante)
    dados={'form':form,'palestrante':palestrante}
    return render(request,'Palestrante/palestrante_form.html',dados)

def palestrante_delete(request,pk):
    palestrante=Palestrante.objects.get(id=pk)
    palestrante.delete()
    return redirect('palestrante_list')

def palestrante_detail(request, pk):
    palestrante=Palestrante.objects.get(id=pk)
    return render(request, 'Palestrante/exibirPalestrante.html', {'palestrante':palestrante})


def participante_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        participantes = Participante.objects.filter(nome__contains=criterio).order_by('nome')
    else:
        participantes = Participante.objects.all().order_by('nome')
        criterio =""
    paginator =Paginator(participantes,10)
    page = request.GET.get('page')
    try:
        participantes = paginator.page(page)
    except PageNotAnInteger:
        participantes=paginator.page(1)
    except EmptyPage:
        participantes = paginator.page(paginator.num_pages)
    dados={'participantes':participantes,'criterio':criterio,'paginator':paginator,'page_obj':participantes}
    return render(request, 'Participante/participante_list.html',dados)

def participante_new(request):
    if (request.method=="POST"):
        form=ParticipanteForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('participante_list')
    else:
        form=ParticipanteForm()
    dados={'form':form}
    return render(request,'Participante/participante_form.html',dados)

def participante_update(request,pk):
    participante=Participante.objects.get(id=pk)
    if (request.method=="POST"):
        form=ParticipanteForm(request.POST,instance=participante)
        if(form.is_valid()):
            form.save()
            return redirect('participante_list')
    else:
        form=ParticipanteForm(instance=participante)
    dados={'form':form,'palestrante':participante}
    return render(request,'Participante/participante_form.html',dados)

def participante_delete(request,pk):
    participante=Participante.objects.get(id=pk)
    participante.delete()
    return redirect('participante_list')

def participante_detail(request, pk):
    participante=Participante.objects.get(id=pk)
    return render(request, 'Participante/exibirParticipante.html', {'participante':participante})

def atividade_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        atividades = Atividade.objects.filter(nome__contains=criterio).order_by('titulo')
    else:
        atividades = Atividade.objects.all().order_by('titulo')
        criterio =""
    paginator =Paginator(atividades,10)
    page = request.GET.get('page')
    try:
        atividades = paginator.page(page)
    except PageNotAnInteger:
        atividades=paginator.page(1)
    except EmptyPage:
        atividades = paginator.page(paginator.num_pages)
    dados={'atividades':atividades,'criterio':criterio,'paginator':paginator,'page_obj':atividades}
    return render(request, 'Atividades/atividade_list.html',dados)

def atividade_new(request):
    if (request.method=="POST"):
        form=AtividadeForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('atividade_list')
    else:
        form=AtividadeForm()
    dados={'form':form}
    return render(request,'Atividades/atividade_form.html',dados)

def atividade_update(request,pk):
    atividade=Atividade.objects.get(id=pk)
    if (request.method=="POST"):
        form=AtividadeForm(request.POST,instance=atividade)
        if(form.is_valid()):
            form.save()
            return redirect('atividade_list')
    else:
        form=AtividadeForm(instance=atividade)
    dados={'form':form,'atividade':atividade}
    return render(request,'Atividades/atividade_form.html',dados)

def atividade_delete(request,pk):
    atividade=Participante.objects.get(id=pk)
    atividade.delete()
    return redirect('atividade_list')

def atividade_detail(request, pk):
    atividade=Atividade.objects.get(id=pk)
    return render(request, 'Atividades/exibirAtividade.html', {'atividade':atividade})


def evento_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        eventos = Evento.objects.filter(nome__contains=criterio).order_by('titulo')
    else:
        eventos = Evento.objects.all().order_by('titulo')
        criterio =""
    paginator =Paginator(eventos,10)
    page = request.GET.get('page')
    try:
        eventos = paginator.page(page)
    except PageNotAnInteger:
        eventos=paginator.page(1)
    except EmptyPage:
        eventos = paginator.page(paginator.num_pages)
    dados={'eventos':eventos,'criterio':criterio,'paginator':paginator,'page_obj':eventos}
    return render(request, 'Evento/evento_list.html',dados)

def evento_new(request):
    if (request.method=="POST"):
        form=EventoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('evento_list')
    else:
        form=EventoForm()
    dados={'form':form}
    return render(request,'Evento/evento_form.html',dados)

def evento_update(request,pk):
    evento=Evento.objects.get(id=pk)
    if (request.method=="POST"):
        form=EventoForm(request.POST,instance=evento)
        if(form.is_valid()):
            form.save()
            return redirect('evento_list')
    else:
        form=EventoForm(instance=evento)
    dados={'form':form,'evento':evento}
    return render(request,'Evento/evento_form.html',dados)

def evento_delete(request,pk):
    evento=Evento.objects.get(id=pk)
    evento.delete()
    return redirect('evento_list')

def evento_detail(request, pk):
    evento=Evento.objects.get(id=pk)
    return render(request, 'Evento/exibirEvento.html', {'evento':evento})



def endereco_list(request):
    criterio = request.GET.get('criterio')
    if criterio:
        enderecos = Endereco.objects.filter(nome__contains=criterio).order_by('logradouro')
    else:
        enderecos = Endereco.objects.all().order_by('logradouro')
        criterio =""
    paginator =Paginator(enderecos,10)
    page = request.GET.get('page')
    try:
        enderecos = paginator.page(page)
    except PageNotAnInteger:
        enderecos=paginator.page(1)
    except EmptyPage:
        enderecos = paginator.page(paginator.num_pages)
    dados={'enderecos':enderecos,'criterio':criterio,'paginator':paginator,'page_obj':enderecos}
    return render(request, 'Endereco/endereco_list.html',dados)

def endereco_new(request):
    if (request.method=="POST"):
        form=EnderecoForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('endereco_list')
    else:
        form=EnderecoForm()
    dados={'form':form}
    return render(request,'Endereco/endereco_form.html',dados)

def endereco_update(request,pk):
    evento=Endereco.objects.get(id=pk)
    if (request.method=="POST"):
        form=EventoForm(request.POST,instance=evento)
        if(form.is_valid()):
            form.save()
            return redirect('endereco_list')
    else:
        form=EventoForm(instance=evento)
    dados={'form':form,'evento':evento}
    return render(request,'Endereco/endereco_form.html',dados)

def endereco_delete(request,pk):
    endereco=Endereco.objects.get(id=pk)
    endereco.delete()
    return redirect('endereco_list')

def endereco_detail(request, pk):
    endereco=Endereco.objects.get(id=pk)
    return render(request, 'Endereco/exibirEndereco.html', {'endereco':endereco})

def atividade_participante(request):
    if (request.method=="POST"):
        form=Atividade_ParticipanteForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('atividade_list')
    else:
        form=Atividade_ParticipanteForm()
    dados={'form':form}
    return render(request,'Atividades/Atividade_Participante_form.html',dados)

def participantes_atividade_list(request, pk):
    resultado = Participante_atividade.objects.filter(atividade_id=pk)
    p = []
    for participantes in resultado:
         p.append(participantes.participante.nome)
    dados={'participantes':p}
    return render(request, 'Atividades/participantes_list.html', dados)

