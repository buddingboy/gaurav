from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    #url(r'^past/procedure_and_policies/$', views.procedure_and_policies, name='procedure_and_policies'),
]