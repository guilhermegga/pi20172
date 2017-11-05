from django.conf.urls import url
from core.views import home, todos_posts, novo, atualiza, deletar, teste_grafico

urlpatterns = [
    url(r'^$', home),
    url(r'^posts', todos_posts, name='posts'),
    url(r'^novo', novo),
    url(r'^grafico', teste_grafico,name='grafico'),

    url(r'^atualizar/(?P<id>\d+)/$', atualiza, name='atualizar'),
    url(r'^deletar/(?P<id>\d+)/$', deletar, name='deletar'),
]
