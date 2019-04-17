from django.core.serializers import json
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext, context
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView, FormView
from .models import CLIENTE, CABELELEIRO, SERVICO, AGENDAMENTO, PRODUTO
from decimal import Decimal
from datetime import date, datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

## CLIENTES
@login_required
def indexCliente(request):
    clientes = CLIENTE.objects.all()
    context = {'clientes' : clientes}
    return render(request, 'website/cliente/index.html',context)

@login_required
def createCliente(request):
    cliente = CLIENTE()
    if request.method == 'POST':
        cliente.APELIDO = request.POST['apelido']
        cliente.SENHA = request.POST['senha']
        cliente.NOME = request.POST['nome']
        cliente.EMAIL = request.POST['email']
        cliente.CELULAR =  request.POST['celular']
        cliente.save()
        return HttpResponseRedirect('/cliente')
    else:
        return render(request, 'website/cliente/create.html')

def editCliente(request, id):
    cliente = CLIENTE.objects.get(id=id)
    context = {'clientes': cliente}
    return render(request, 'website/cliente/edit.html', context)

def updateCliente(request, id):
    cliente = CLIENTE.objects.get(id=id)

    cliente.NOME = request.POST['nome']
    cliente.EMAIL = request.POST['email']
    cliente.CELULAR = request.POST['celular']
    cliente.SENHA = request.POST['senha']
    cliente.APELIDO = request.POST['apelido']
    cliente.save()
    return redirect('/cliente')

def deleteCliente(request, id):
    cliente = CLIENTE.objects.get(id=id)
    cliente.delete()
    return redirect('/cliente')

## CABELELEIROS

def indexCabeleleiro(request):
    cabeleleiros = CABELELEIRO.objects.all()
    context = {'cabeleleiros' : cabeleleiros}
    return render(request, 'website/cabeleleiro/index.html',context)

def createCabeleleiro(request):
    cabeleleiro = CABELELEIRO()
    if request.method == 'POST':
        cabeleleiro.SENHA = request.POST['senha']
        cabeleleiro.NOME = request.POST['nome']
        cabeleleiro.EMAIL = request.POST['email']
        cabeleleiro.CELULAR =  request.POST['celular']
        cabeleleiro.save()
        return HttpResponseRedirect('/cabeleleiro')
    else:
        return render(request, 'website/cabeleleiro/create.html')

def editCabeleleiro(request, id):
    cabeleleiro = CABELELEIRO.objects.get(id=id)
    context = {'cabeleleiros': cabeleleiro}
    return render(request, 'website/cabeleleiro/edit.html', context)

def updateCabeleleiro(request, id):
    cabeleleiro = CABELELEIRO.objects.get(id=id)

    cabeleleiro.NOME = request.POST['nome']
    cabeleleiro.EMAIL = request.POST['email']
    cabeleleiro.CELULAR = request.POST['celular']
    cabeleleiro.SENHA = request.POST['senha']
    cabeleleiro.save()
    return redirect('/cabeleleiro')

def deleteCabeleleiro(request, id):
    cabeleleiro = CABELELEIRO.objects.get(id=id)
    cabeleleiro.delete()
    return redirect('/cabeleleiro')


## Produtos

def editProduto(request, id):
    produto = PRODUTO.objects.get(id=id)
    context = {'produtos': produto}
    return render(request, 'website/produto/edit.html', context)

def updateProduto(request, id):
    produto = PRODUTO.objects.get(id=id)

    produto.NOME = request.POST['nome']
    valor = request.POST['valor']
    produto.VALOR_UNITARIO = Decimal(valor.replace(',', '.'))
    produto.QUANTIDADE = request.POST['quant']
    produto.save()
    messages.info(request, 'Alterações salvas com sucesso');
    return redirect('/produto')

def deleteProduto(request, pk):
    produto = PRODUTO.objects.get(id=pk)
    produto.delete()
    messages.info(request, 'Produto excluído');
    return HttpResponseRedirect(reverse_lazy('website:indexProduto'))

## Servicos

def indexServico(request):
    servicos = SERVICO.objects.all()
    context = {'servicos' : servicos}
    return render(request, 'website/servico/index.html',context)

def createServico(request):
    servico = SERVICO()
    if request.method == 'POST':
        servico.NOME = request.POST['nome']
        valor = request.POST['valor']
        servico.VALOR = Decimal(valor.replace(',',''))
        servico.save()
        return HttpResponseRedirect('/servico')
    else:
        return render(request, 'website/servico/create.html')

def editServico(request, id):
    servico = SERVICO.objects.get(id=id)
    context = {'servicos': servico}
    return render(request, 'website/servico/edit.html', context)

def updateServico(request, id):
    servico = SERVICO.objects.get(id=id)

    servico.NOME = request.POST['nome']
    valor = request.POST['valor']
    servico.VALOR = Decimal(valor.replace(',', '.'))
    servico.save()
    return redirect('/servico')

def deleteServico(request, id):
    servico = SERVICO.objects.get(id=id)
    servico.delete()
    return redirect('/servico')

#AGENDAMENTO
def indexAgendamento(request):
    agendamentos = AGENDAMENTO.objects.all()
    context = {'agendamentos' : agendamentos}
    return render(request, 'website/agenda/index.html',context)

def createAgendamento(request):
    agendamento = AGENDAMENTO()
    if request.method == 'POST':
        servico = SERVICO.objects.get(id=int( request.POST['servico']))
        cliente = CLIENTE.objects.get(id=int(request.POST['cliente']))
        cabeleleiro = CABELELEIRO.objects.get(id=int(request.POST['cabeleleiro']))
        agendamento.DATA_INICIO = request.POST['data_inicio']
        agendamento.DATA_FIM = request.POST['data_fim']
        agendamento.CLIENTES =  cliente
        agendamento.CABELELEIROS = cabeleleiro
        agendamento.SERVICOS = servico
        agendamento.save()
        return HttpResponseRedirect('/agenda')
    else:
        clientes = CLIENTE.objects.all()
        servicos = SERVICO.objects.all()
        cabeleleiros = CABELELEIRO.objects.all()

        context = {'clientes' : clientes,'servicos' : servicos,'cabeleleiros' : cabeleleiros}
        return render(request, 'website/agenda/create.html',context)

def editAgendamento(request, id):
    agendamentos = AGENDAMENTO.objects.get(id=id)
    clientes = CLIENTE.objects.all()
    servicos = SERVICO.objects.all()
    cabeleleiros = CABELELEIRO.objects.all()
    agendamentos.DATA = agendamentos.DATA
    context = {'agendamentos': agendamentos, 'clientes' : clientes,'servicos' : servicos,'cabeleleiros' : cabeleleiros}
    return render(request, 'website/agenda/edit.html', context)

def updateAgendamento(request, id):
    agendamento = AGENDAMENTO.objects.get(id=id)
    servico = SERVICO.objects.get(id=int(request.POST['servico']))
    cliente = CLIENTE.objects.get(id=int(request.POST['cliente']))
    cabeleleiro = CABELELEIRO.objects.get(id=int(request.POST['cabeleleiro']))
    agendamento.DATA = request.POST['data']
    agendamento.HORA_INICIO = request.POST['hora']
    agendamento.HORA_FIM = request.POST['hora']
    agendamento.CLIENTES = cliente
    agendamento.CABELELEIROS = cabeleleiro
    agendamento.SERVICOS = servico
    agendamento.save()

    return redirect('/agenda')

def deleteAgendamento(request, id):
    agendamento = AGENDAMENTO.objects.get(id=id)
    agendamento.delete()
    return redirect('/agenda')

def testAgendamento(request):
    all_events = AGENDAMENTO.objects.all()
    #get_event_types = Events.objects.only('event_type')

    if request.GET:
        event_arr = []
        if request.GET.get('event_type') == "all":
            all_events = AGENDAMENTO.objects.all()
     #   else:
     #       all_events = AGENDAMENTO.objects.filter(event_type__icontains=request.GET.get('event_type'))

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.event_name
            start_date = datetime.datetime.strptime(str(i.DATA.date()), "%Y-%m-%d %H:%M:%S'").strftime("%Y-%m-%d %H:%M:%S'")
            end_date = datetime.datetime.strptime(str(i.DATA.date()), "%Y-%m-%d %H:%M:%S'").strftime("%Y-%m-%d %H:%M:%S'")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {"events":all_events}
    return render(request, 'website/agenda/calendar.html',context)


class CreateUserForm(FormView):
    form_class = UserCreationForm
    template_name = "registration/register.html"

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'website/calendar.html'

class RegisterView(TemplateView):
    template_name = 'registration/register.html'

class HomeView(TemplateView):
    template_name = 'website/home.html'

class ProdutoCreateView(CreateView):
    model = PRODUTO
    template_name = 'website/produto/create.html'
    fields = ['NOME', 'QUANTIDADE', 'VALIDADE_PRODUTO', 'VALOR_UNITARIO', 'ESPECIFICACAO']
    success_url = reverse_lazy('website:indexProduto')

class ProdutoListView(ListView):
    model = PRODUTO
    template_name = 'website/produto/index.html'



def get_data(request):
    data = [
        dict(title='Lunch', start='2018-10-22 10:00', end='2018-10-22 10:30', allDay=False, className='event-azure'),
        dict(title='Lunch', start='2018-10-23 11:00', end='2018-10-22 11:30', allDay=False, className='event-orange'),
        dict(title='Lunch', start='2018-10-24 12:00', end='2018-10-22 12:30', allDay=False, className='event-green'),
        dict(title='Lunch', start='2018-10-25 13:00', end='2018-10-22 13:30', allDay=False, className='event-red'),
        dict(title='Lunch', start='2018-10-26 14:00', end='2018-10-22 14:30', allDay=False, className='event-blue')
    ]
    return JsonResponse(data, safe=False)
