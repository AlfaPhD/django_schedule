from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class cabeleireiro(models.Model):
    user = models.OneToOneField(
        verbose_name="Usuário", related_name='cabeleireiro',
        to=User, on_delete=models.PROTECT
    )
    email = models.EmailField("email", max_length=100)
    nome = models.CharField("nome", max_length=30)
    senha = models.CharField("senha", max_length=200)
    celular = models.CharField("celular", max_length=30)
    ativo = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.nome


class cliente(models.Model):
    user = models.OneToOneField(
        verbose_name="Usuário", related_name='cliente',
        to=User, on_delete=models.PROTECT
    )
    apelido = models.CharField("apelido", max_length=100)
    senha = models.CharField("senha", max_length=30)
    nome = models.CharField("nome", max_length=100)
    email = models.EmailField("email", max_length=200)
    celular = models.CharField("celular", max_length=30)
    def __str__(self):
        return self.nome


class servico(models.Model):
    nome = models.CharField("nome", max_length=30)
    valor = models.DecimalField("valor", max_digits=5, decimal_places=2)
    url = models.URLField("url", null=True,blank=True,max_length=500)
    def __str__(self):
        return self.nome


class produto(models.Model):
    nome = models.CharField("nome", max_length=100)
    quantidade = models.IntegerField("quantidade")
    validade_produto = models.DateField("validade_produto")
    valor_unitario = models.DecimalField("valor_unitario", max_digits=5, decimal_places=2)
    especificacao = models.CharField("especificacao", max_length=400)

    def __str__(self):
        return self.nome



class estoque(models.Model):
    quantidade = models.IntegerField("quantidade")
    data_saida = models.DateField("data_saida")
    id_produto = models.ManyToManyField("produto")


class agendamento(models.Model):
    status = models.CharField("status", max_length=30)
    data = models.DateField("data")
    hora_inicio = models.TimeField("hora_inicio")
    hora_fim = models.TimeField("hora_fim")
    clientes = models.ForeignKey(
        cliente,
		 related_name='clientes',
        on_delete=models.CASCADE
    )
    produtos = models.ManyToManyField(
        produto,
        related_name='produtos'
    )
    cabeleireiros = models.ForeignKey(
        cabeleireiro,
		related_name='cabeleireiros',
        on_delete=models.CASCADE
    )
    servicos = models.ManyToManyField(
        servico,
        related_name='servicos'
    )



