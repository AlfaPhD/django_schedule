from rest_framework import serializers
from website.models import CABELELEIRO,  CLIENTE, SERVICO, AGENDAMENTO, PRODUTO, ESTOQUE

class CabeleleiroSerializer(serializers.ModelSerializer):

    class Meta:
        model = CABELELEIRO
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CLIENTE
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SERVICO
        fields = '__all__'


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AGENDAMENTO
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRODUTO
        fields = '__all__'


class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESTOQUE
        fields = '__all__'