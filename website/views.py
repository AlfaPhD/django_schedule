from django.core.serializers import json
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext, context
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView, FormView
from .models import cliente, cabeleireiro, servico, agendamento, produto
from decimal import Decimal
from datetime import date, datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponseForbidden
from django.contrib.auth import logout as auth_logout


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("website:index")

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
                    "form": form
              }
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            print(">>>>>>>>>>>>>", form.cleaned_data)
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            #celular = form.cleaned_data.get("celular")
            password = form.cleaned_data.get("password")
            new_user = User.objects.create_user(username, email, password)
            cli = cliente(
                user=new_user,
                apelido=username,
                #celular=celular,
                email=email
            )
            cli.save()
            return render(request, 'registration/login.html', context)
        else:
            return render(request, "registration/register.html", context)
    return render(request, "registration/register.html", context)



## clientes
@login_required
def indexCliente(request):
    clientes = cliente.objects.all()
    context = {'clientes' : clientes}
    return render(request, 'website/cliente/index.html',context)

@login_required
def PerfilCliente(request, id):
    clientes = cliente.objects.get(id=id)
    context = {'clientes': clientes}
    return render(request, 'website/cliente/perfil.html', context)


@login_required
def createCliente(request):
    clientes = cliente()
    if request.method == 'POST':
        clientes.apelido= request.POST['apelido']
        clientes.senha = request.POST['senha']
        clientes.nome = request.POST['nome']
        clientes.email = request.POST['email']
        clientes.celular =  request.POST['celular']
        clientes.save()
        return HttpResponseRedirect('/cliente')
    else:
        return render(request, 'website/cliente/create.html')


@login_required
def editCliente(request, id):
    clientes = cliente.objects.get(id=id)
    context = {'clientes': clientes}
    return render(request, 'website/cliente/edit.html', context)

def updateCliente(request, id):
    clientes = cliente.objects.get(id=id)

    clientes.nome = request.POST['nome']
    clientes.email = request.POST['email']
    clientes.celular = request.POST['celular']
    clientes.senha = request.POST['senha']
    clientes.apelido = request.POST['apelido']
    clientes.save()
    return redirect('/cliente')


@login_required
def deleteCliente(request, id):
    clientes = cliente.objects.get(id=id)
    clientes.delete()
    return redirect('/cliente')

## cabeleireiros


@login_required
def indexcabeleireiro(request):
    user = request.user
    try:
        user.cabeleireiro
    except cabeleireiro.DoesNotExist:
        return HttpResponseForbidden()
    cabeleleiros = cabeleireiro.objects.all()
    context = {'cabeleleiros': cabeleleiros}
    return render(request, 'website/cabeleireiro/index.html', context)


@login_required
def createcabeleireiro(request):
    cabeleireiros = cabeleireiro()
    if request.method == 'POST':
        cabeleireiros.senha = request.POST['senha']
        cabeleireiros.nome = request.POST['nome']
        cabeleireiros.email = request.POST['email']
        cabeleireiros.celular =  request.POST['celular']
        cabeleireiros.save()
        return HttpResponseRedirect('/cabeleireiro')
    else:
        return render(request, 'website/cabeleireiro/create.html')


@login_required
def editcabeleireiro(request, id):
    cabeleireiros = cabeleireiro.objects.get(id=id)
    context = {'cabeleireiros': cabeleireiros}
    return render(request, 'website/cabeleireiro/edit.html', context)


@login_required
def updatecabeleireiro(request, id):
    cabeleireiros = cabeleireiro.objects.get(id=id)

    cabeleireiros.nome = request.POST['nome']
    cabeleireiros.email = request.POST['email']
    cabeleireiros.celular = request.POST['celular']
    cabeleireiros.senha = request.POST['senha']
    cabeleireiros.save()
    return redirect('/cabeleireiro')


@login_required
def deletecabeleireiro(request, id):
    cabeleireiross = cabeleireiro.objects.get(id=id)
    cabeleireiross.delete()
    return redirect('/cabeleireiro')


## Produtos


@login_required
def editProduto(request, id):
    produtos = produto.objects.get(id=id)
    context = {'produtos': produtos}
    return render(request, 'website/produto/edit.html', context)


@login_required
def updateProduto(request, id):
    produtos = produto.objects.get(id=id)

    produtos.nome = request.POST['nome']
    valor = request.POST['valor']
    produtos.valor_unitario= Decimal(valor.replace(',', '.'))
    produtos.quantidade = request.POST['quant']
    produtos.save()
    messages.info(request, 'Alterações salvas com sucesso');
    return redirect('/produto')


@login_required
def deleteProduto(request, pk):
    produtos = produto.objects.get(id=pk)
    produtos.delete()
    messages.info(request, 'Produto excluído');
    return HttpResponseRedirect(reverse_lazy('website:indexProduto'))

## Servicos


@login_required
def indexServico(request):
    servicos = servico.objects.all()
    context = {'servicos' : servicos}
    return render(request, 'website/servico/index.html',context)


@login_required
def createServico(request):
    servicos = servico()
    if request.method == 'POST':
        servicos.nome= request.POST['nome']
        valor = request.POST['valor']
        servicos.valor = Decimal(valor.replace(',',''))
        servicos.save()
        return HttpResponseRedirect('/servico')
    else:
        return render(request, 'website/servico/create.html')


@login_required
def editServico(request, id):
    servicos = servico.objects.get(id=id)
    context = {'servicos': servicos}
    return render(request, 'website/servico/edit.html', context)


@login_required
def updateServico(request, id):
    servicos = servico.objects.get(id=id)

    servicos.nome = request.POST['nome']
    valor = request.POST['valor']
    servicos.valor = Decimal(valor.replace(',', '.'))
    servicos.save()
    return redirect('/servico')


@login_required
def deleteServico(request, id):
    servicos = servico.objects.get(id=id)
    servicos.delete()
    return redirect('/servico')

#agendamento

@login_required
def indexAgendamento(request):
    agendamentos = agendamento.objects.all()
    context = {'agendamentos' : agendamentos}
    return render(request, 'website/agenda/index.html',context)


@login_required
def createAgendamento(request):
    agendamentos = agendamento()
    if request.method == 'POST':
        servicos = servico.objects.get(id=int(request.POST['servico']))
        clientes = cliente.objects.get(id=int(request.POST['cliente']))
        cabeleireiros = cabeleireiro.objects.get(id=int(request.POST['cabeleireiro']))
        agendamentos.data_inicio= request.POST['data_inicio']
        agendamentos.data_fim = request.POST['data_fim']
        agendamentos.clientes =  clientes
        agendamentos.cabeleireiros = cabeleireiros
        agendamentos.servicos = servicos
        agendamentos.save()
        return HttpResponseRedirect('/agenda')
    else:
        clientes = cliente.objects.all()
        servicos = servico.objects.all()
        cabeleireiros = cabeleireiro.objects.all()

        context = {'clientes' : clientes,'servicos' : servicos,'cabeleireiros' : cabeleireiros}
        return render(request, 'website/agenda/create.html',context)


@login_required
def editAgendamento(request, id):
    agendamentos = agendamento.objects.get(id=id)
    clientes = cliente.objects.all()
    servicos = servico.objects.all()
    cabeleireiros = cabeleireiro.objects.all()
    agendamentos.data_inicio = agendamentos.data_inicio
    context = {'agendamentos': agendamentos, 'clientes' : clientes,'servicos' : servicos,'cabeleireiros' : cabeleireiros}
    return render(request, 'website/agenda/edit.html', context)


@login_required
def updateAgendamento(request, id):
    agendamentos = agendamento.objects.get(id=id)
    servicos = servico.objects.get(id=int(request.POST['servico']))
    clientes = cliente.objects.get(id=int(request.POST['cliente']))
    cabeleireiros = cabeleireiro.objects.get(id=int(request.POST['cabeleireiro']))
    agendamentos.data_inicio= request.POST['data']
    agendamentos.clientes = clientes
    agendamentos.cabeleireiros = cabeleireiros
    agendamentos.servicos = servicos
    agendamentos.save()

    return redirect('/agenda')


@login_required
def deleteAgendamento(request, id):
    agendamentos = agendamento.objects.get(id=id)
    agendamentos.delete()
    return redirect('/agenda')


@login_required
def testAgendamento(request):
    all_events = agendamento.objects.all()
    #get_event_types = Events.objects.only('event_type')

    if request.GET:
        event_arr = []
        if request.GET.get('event_type') == "all":
            all_events = agendamento.objects.all()
     #   else:
     #       all_events = agendamento.objects.filter(event_type__icontains=request.GET.get('event_type'))

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
    success_url = reverse_lazy('website:login')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'website/calendar.html'
    extra_context = {
        'cabeleireiros': cabeleireiro.objects.all(),
        'produtos': produto.objects.all(),
        'servicos': servico.objects.all()
    }


class HomeView(TemplateView):
    template_name = 'website/home.html'

class ProdutoCreateView(CreateView):
    model = produto
    template_name = 'website/produto/create.html'
    fields = ['nome', 'quantidade', 'validade_produto', 'valor_unitario', 'especificacao']
    success_url = reverse_lazy('website:indexProduto')

class ProdutoListView(ListView):
    model = produto
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
