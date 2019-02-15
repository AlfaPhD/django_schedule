from django.db import models

# Create your models here.
class CABELELEIRO(models.Model):
    EMAIL = models.CharField("EMAIL", max_length=100)
    NOME = models.CharField("NOME", max_length=30)
    SENHA = models.EmailField("SENHA", max_length=200)
    CELULAR = models.CharField("CELULAR", max_length=30)

class CLIENTE(models.Model):
    APELIDO = models.CharField("APELIDO", max_length=100)
    SENHA = models.CharField("SENHA", max_length=30)
    NOME = models.CharField("NOME", max_length=100)
    EMAIL = models.EmailField("EMAIL", max_length=200)
    CELULAR = models.CharField("CELULAR", max_length=30)


class SERVICO(models.Model):
    NOME = models.CharField("NOME", max_length=30)
    VALOR = models.DecimalField("VALOR", max_digits=5 ,decimal_places=2)

class PRODUTO(models.Model):
    NOME = models.CharField("NOME", max_length=100)
    QUANTIDADE = models.IntegerField("QUANTIDADE")
    VALIDADE_PRODUTO = models.DateField("VALIDADE_PRODUTO")
    VALOR_UNITARIO = models.DecimalField("VALOR_UNITARIO", max_digits=5 ,decimal_places=2)
    ESPECIFICACAO = models.CharField("ESPECIFICACAO", max_length=400)

class ESTOQUE(models.Model):
    QUANTIDADE = models.IntegerField("QUANTIDADE")
    DATA_SAIDA = models.DateField("DATA_SAIDA")
    ID_PRODUTO = models.ManyToManyField("PRODUTO")

class AGENDAMENTO(models.Model):
    DATA = models.DateField("DATA")
    HORA_INICIO = models.TimeField("HORA_INICIO")
    HORA_FIM = models.TimeField("HORA_FIM")
    CLIENTES = models.ForeignKey(
        CLIENTE,
        on_delete=models.CASCADE
    )
    CABELELEIROS = models.ForeignKey(
        CABELELEIRO,
        on_delete=models.CASCADE
    )
    SERVICOS = models.ForeignKey(
        SERVICO,
        on_delete=models.CASCADE
    )



