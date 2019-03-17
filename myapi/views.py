from website.models import  CABELELEIRO,  CLIENTE, SERVICO, AGENDAMENTO, PRODUTO, ESTOQUE
from .serializers import CabeleleiroSerializer, ClienteSerializer, ServicoSerializer, AgendamentoSerializer, ProdutoSerializer, EstoqueSerializer

from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser, AllowAny
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication

# Create your views here.
class CabeleleiroList(generics.ListCreateAPIView):

    queryset = CABELELEIRO.objects.all()
    serializer_class = CabeleleiroSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class CabeleleiroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CABELELEIRO.objects.all()
    serializer_class = CabeleleiroSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class ClienteList(generics.ListCreateAPIView):
    queryset = CLIENTE.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CLIENTE.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ServicoList(generics.ListCreateAPIView):
    queryset = SERVICO.objects.all()
    serializer_class = ServicoSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ServicoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SERVICO.objects.all()
    serializer_class = ServicoSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class AgendamentoList(generics.ListCreateAPIView):
    queryset = AGENDAMENTO.objects.all()
    serializer_class = AgendamentoSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class AgendamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AGENDAMENTO.objects.all()
    serializer_class = AgendamentoSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ProdutoList(generics.ListCreateAPIView):
    queryset = PRODUTO.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PRODUTO.objects.all()
    serializer_class = ProdutoSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class EstoqueList(generics.ListCreateAPIView):
    queryset = ESTOQUE.objects.all()
    serializer_class = EstoqueSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class EstoqueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ESTOQUE.objects.all()
    serializer_class = EstoqueSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'



