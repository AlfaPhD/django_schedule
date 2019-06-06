from website.models import  cabeleireiro,  cliente, servico, agendamento, produto, estoque
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser, AllowAny
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
	
# Create your views here.
class cabeleireiroList(generics.ListCreateAPIView):

    queryset = cabeleireiro.objects.all()
    serializer_class = cabeleireiroSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class cabeleireiroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = cabeleireiro.objects.all()
    serializer_class = cabeleireiroSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class ClienteList(generics.ListCreateAPIView):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ServicoList(generics.ListCreateAPIView):
    queryset = servico.objects.all()
    serializer_class = ServicoSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ServicoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = servico.objects.all()
    serializer_class = ServicoSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class AgendamentoList(generics.ListCreateAPIView):
    queryset = agendamento.objects.all()
    serializer_class = AgendamentoSerializerList
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class AgendamentoPost(generics.ListCreateAPIView):
    queryset = agendamento.objects.all()
    serializer_class = AgendamentoSerializerPost
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class AgendamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = agendamento.objects.all()
    serializer_class = AgendamentoSerializerPost
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'



class ProdutoList(generics.ListCreateAPIView):
    queryset = produto.objects.all()
    serializer_class = ProdutoSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = produto.objects.all()
    serializer_class = ProdutoSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class EstoqueList(generics.ListCreateAPIView):
    queryset = estoque.objects.all()
    serializer_class = EstoqueSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class EstoqueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = estoque.objects.all()
    serializer_class = EstoqueSerializer
    #authentication_classes = [OAuth2Authentication, SessionAuthentication]
    #permission_classes = [IsAdminUser]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'



