from django.db import models

# Create your models here.
class cabeleleiro(models.Model):
    email = models.EmailField("email", max_length=100)
    nome = models.CharField("nome", max_length=30)
    senha = models.CharField("senha", max_length=200)
    celular = models.CharField("celular", max_length=30)

class cliente(models.Model):
    apelido = models.CharField("apelido", max_length=100)
    senha = models.CharField("senha", max_length=30)
    nome = models.CharField("nome", max_length=100)
    email = models.EmailField("email", max_length=200)
    celular = models.CharField("celular", max_length=30)


class servico(models.Model):
    nome = models.CharField("nome", max_length=30)
    valor = models.DecimalField("valor", max_digits=5, decimal_places=2)

class produto(models.Model):
    nome = models.CharField("nome", max_length=100)
    quantidade = models.IntegerField("quantidade")
    validade_produto = models.DateField("validade_produto")
    valor_unitario = models.DecimalField("valor_unitario", max_digits=5, decimal_places=2)
    especificacao = models.CharField("especificacao", max_length=400)

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
    cabeleleiros = models.ForeignKey(
        cabeleleiro,
		related_name='cabeleleiros',
        on_delete=models.CASCADE
    )
    servicos = models.ForeignKey(
        servico,
		related_name='servicos',
        on_delete=models.CASCADE
    )



