from django.urls import path

from .views import index, cameras_view, condominio, config, agenda, contatos, informacoes, ocorrencias, servicos, solicitacoes, telefones, unidades, internets

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('unidades', views.unidades, name='unidades'),
    path('internets', views.internets, name='internets'),
    path('condominio', views.condominio, name='condominio'),
    path('agendamento', agenda, name='menu_agenda'),
    path('adm', config, name='menu_adm'),
    path('contatos', contatos, name='menu_contatos'),
    path('informacoes', informacoes, name='menu_informacoes'),
    path('ocorrencias', ocorrencias, name='menu_ocorrencias'),
    path('servicos', servicos, name='menu_servicos'),
    path('solicitacoes', solicitacoes, name='menu_solicitacoes'),
    path('telefones', telefones, name='menu_telefones'),
    path('cameras/', views.cameras_view, name='cameras_view'),

]

