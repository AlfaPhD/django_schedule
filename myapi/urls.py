
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^apicabeleleiros/$', views.CabeleleiroList.as_view(), name='cabeleleiro-list'),
    url(r'^apicabeleleiros/(?P<pk>[0-9]+)/$', views.CabeleleiroDetail.as_view(), name='cabeleleiro-detail'),

    url(r'^apicliente/$', views.ClienteList.as_view()),
    url(r'^apicliente/(?P<pk>[0-9]+)/$', views.ClienteDetail.as_view()),

    url(r'^apiservico/$', views.ServicoList.as_view()),
    url(r'^apiservico/(?P<pk>[0-9]+)/$', views.ServicoDetail.as_view()),

    url(r'^apiagendamento/$', views.AgendamentoList.as_view()),
    url(r'^apiagendamento/(?P<pk>[0-9]+)/$', views.AgendamentoDetail.as_view()),

    url(r'^apiproduto/$', views.ProdutoList.as_view()),
    url(r'^apiproduto/(?P<pk>[0-9]+)/$', views.ProdutoDetail.as_view()),

    url(r'^apiestoque/$', views.EstoqueList.as_view()),
    url(r'^apiestoque/(?P<pk>[0-9]+)/$', views.EstoqueDetail.as_view()),

]