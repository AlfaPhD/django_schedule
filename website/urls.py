from django.urls import path
from . import views
from django.contrib.auth.urls import views as auth_views


app_name = 'website'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('home', views.HomeView.as_view(), name='home'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('cadastrar', views.register_page, name='cadastrar'),
    #Cliente
    path('cliente/', views.indexCliente, name='indexCliente'),
    path('cliente/create', views.createCliente, name='createCliente'),
    path('cliente/edit/<int:id>', views.editCliente, name='editCliente'),
    path('cliente/edit/<int:id>', views.editPerfil, name='editPerfil'),
    path('cliente/perfil/<int:id>', views.PerfilCliente, name='perfilCliente'),
    path('cliente/edit/update/<int:id>', views.updateCliente, name='updateCliente'),
    path('cliente/deletar/<int:id>', views.deleteCliente, name='deleteCliente'),

    #cabeleireiro
    path('cabeleireiro/', views.indexcabeleireiro, name='indexcabeleireiro'),
    path('cabeleireiro/create', views.createcabeleireiro, name='createcabeleireiro'),
    path('cabeleireiro/edit/<int:id>', views.editcabeleireiro, name='editcabeleireiro'),
    path('cabeleireiro/edit/update/<int:id>', views.updatecabeleireiro, name='updatecabeleireiro'),
    path('cabeleireiro/deletar/<int:id>', views.deletecabeleireiro, name='deletecabeleireiro'),

    # Produto
    path('produto/', views.ProdutoListView.as_view(), name='indexProduto'),
    path('produto/create', views.ProdutoCreateView.as_view(), name='createProduto'),
    path('produto/edit/<int:id>', views.editProduto, name='editProduto'),
    path('produto/edit/update/<int:id>', views.updateProduto, name='updateProduto'),
    path('produto/deletar/<int:pk>', views.deleteProduto, name='deleteProduto'),

    # Servico
    path('servico/', views.indexServico, name='indexServico'),
    path('servico/create', views.createServico, name='createServico'),
    path('servico/edit/<int:id>', views.editServico, name='editServico'),
    path('servico/edit/update/<int:id>', views.updateServico, name='updateServico'),
    path('servico/deletar/<int:id>', views.deleteServico, name='deleteServico'),

    # Agenda
    path('agenda/', views.indexAgendamento, name='indexAgendamento'),
    path('agenda/create', views.createAgendamento, name='createAgendamento'),
    path('agenda/edit/<int:id>', views.editAgendamento, name='editAgendamento'),
    path('agenda/edit/update/<int:id>', views.updateAgendamento, name='updateAgendamento'),
    path('agenda/deletar/<int:id>', views.deleteAgendamento, name='deleteAgendamento'),

    path('teste/', views.testAgendamento, name='testAgendamento'),
    path('get-data', views.get_data, name='get-data'),
]
