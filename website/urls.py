from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('get-data', views.get_data, name='get-data'),
]
