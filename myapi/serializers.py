from rest_framework import serializers
from website.models import cabeleleiro,  cliente, servico, agendamento, produto, estoque

class CabeleleiroSerializer(serializers.ModelSerializer):

    class Meta:
        model = cabeleleiro
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = cliente
        fields = '__all__'

class ServicoSerializer(serializers.ModelSerializer):

    class Meta:
        model = servico
        fields = '__all__'


class AgendamentoSerializer(serializers.ModelSerializer):
	cabeleleiro_nome = serializers.StringRelatedField(many=True)
	cliente_nome = serializers.StringRelatedField(many=True)
	servico_nome = serializers.StringRelatedField(many=True)

	class Meta:
		model = agendamento
		fields = "__all__"


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = '__all__'


class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = estoque
        fields = '__all__'