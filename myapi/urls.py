
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^apiuser/$', views.UserList.as_view(), name='user-list'),
    url(r'^apiuser/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
	
    url(r'^apicabeleireiros/$', views.cabeleireiroList.as_view(), name='cabeleireiro-list'),
    url(r'^apicabeleireiros/(?P<pk>[0-9]+)/$', views.cabeleireiroDetail.as_view(), name='cabeleireiro-detail'),

    url(r'^apicliente/$', views.ClienteList.as_view()),
    url(r'^apicliente/(?P<pk>[0-9]+)/$', views.ClienteDetail.as_view()),

    url(r'^apiservico/$', views.ServicoList.as_view()),
    url(r'^apiservico/(?P<pk>[0-9]+)/$', views.ServicoDetail.as_view()),

    url(r'^apiagendamento/$', views.AgendamentoList.as_view()),
    url(r'^apiagendamentoPost/$', views.AgendamentoPost.as_view()),
    url(r'^apiagendamento/(?P<pk>[0-9]+)/$', views.AgendamentoDetail.as_view()),

    url(r'^apiproduto/$', views.ProdutoList.as_view()),
    url(r'^apiproduto/(?P<pk>[0-9]+)/$', views.ProdutoDetail.as_view()),

    url(r'^apiestoque/$', views.EstoqueList.as_view()),
    url(r'^apiestoque/(?P<pk>[0-9]+)/$', views.EstoqueDetail.as_view()),

]