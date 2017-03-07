from django.conf.urls import url
from django.contrib.auth.views import login,logout

from apppalestras.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/', login, {'template_name': 'utils/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'home'}, name='logout'),
    url(r'^palestrante/list$', palestrante_list, name='palestrante_list'),
    url(r'^palestrante/detail/(?P<pk>\d+)$',
        palestrante_detail, name='palestrante_detail'),
    url(r'^palestrante/new/$', palestrante_new, name='palestrante_new'),
    url(r'^palestrante/update/(?P<pk>\d+)$',
        palestrante_update, name='palestrante_update'),
    url(r'^palestrante/delete/(?P<pk>\d+)$',
        palestrante_delete, name='palestrante_delete'),

    url(r'^participante/list$', participante_list, name='participante_list'),
    url(r'^participante/detail/(?P<pk>\d+)$',
        participante_detail, name='participante_detail'),
    url(r'^participante/new/$', participante_new, name='participante_new'),
    url(r'^participante/update/(?P<pk>\d+)$',
        participante_update, name='participante_update'),
    url(r'^participante/delete/(?P<pk>\d+)$',
        participante_delete, name='participante_delete'),

    url(r'^atividade/list$', atividade_list, name='atividade_list'),
    url(r'^atividade/detail/(?P<pk>\d+)$',
        atividade_detail, name='atividade_detail'),
    url(r'^atividade/new/$', atividade_new, name='atividade_new'),
    url(r'^atividade/update/(?P<pk>\d+)$',
        atividade_update, name='atividade_update'),
    url(r'^atividade/delete/(?P<pk>\d+)$',
        atividade_delete, name='atividade_delete'),

    url(r'^evento/list$', evento_list, name='evento_list'),
    url(r'^evento/detail/(?P<pk>\d+)$',
        evento_detail, name='evento_detail'),
    url(r'^evento/new/$', evento_new, name='evento_new'),
    url(r'^evento/update/(?P<pk>\d+)$',
        evento_update, name='evento_update'),
    url(r'^evento/delete/(?P<pk>\d+)$',
        evento_delete, name='evento_delete'),

    url(r'^endereco/list$', endereco_list, name='endereco_list'),
    url(r'^endereco/detail/(?P<pk>\d+)$',
        endereco_detail, name='endereco_detail'),
    url(r'^endereco/new/$', endereco_new, name='endereco_new'),
    url(r'^endereco/update/(?P<pk>\d+)$',
        endereco_update, name='endereco_update'),
    url(r'^endereco/delete/(?P<pk>\d+)$',
        endereco_delete, name='endereco_delete'),

    url(r'^atividade/participante/new/$', atividade_participante, name='atividade_participante'),
    url(r'^participante/atividade/list/(?P<pk>\d+)$', participantes_atividade_list, name='participantes_atividade_list'),
]