from django.conf.urls import url
from result_pi.views import home

urlpatterns = [
    url(r'^$',home),
]
