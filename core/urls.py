from django.conf.urls import url
from core.views import home, todos_posts, novo, atualiza, deletar, teste_grafico,testeGrafico2

urlpatterns = [
    url(r'^$', home),
    url(r'^posts', todos_posts, name='posts'),
    url(r'^novo', novo),
    url(r'^grafico', teste_grafico,name='grafico'),
    url(r'^grafico2', testeGrafico2,name='grafico2'),

    url(r'^atualizar/(?P<id>\d+)/$', atualiza, name='atualizar'),
    url(r'^deletar/(?P<id>\d+)/$', deletar, name='deletar'),
]
