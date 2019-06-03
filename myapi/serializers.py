from rest_framework import serializers
from website.models import cabeleireiro,  cliente, servico, agendamento, produto, estoque

class cabeleireiroSerializer(serializers.ModelSerializer):

    class Meta:
        model = cabeleireiro
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = cliente
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = servico
        fields = '__all__'


class AgendamentoSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = agendamento
        fields = ('__all__')

class AgendamentoSerializerList(serializers.ModelSerializer):
    servicos = ServicoSerializer(many=True)
    cabeleireiros = cabeleireiroSerializer()
    clientes = ClienteSerializer()
    class Meta:
        model = agendamento
        fields = ('__all__')

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = '__all__'


class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = estoque
        fields = '__all__'