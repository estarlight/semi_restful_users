from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users$', views.index, name='index'),
    url(r'^users/new$', views.new, name='new'),
    url(r'^users/(?P<id_num>\d+)/edit$', views.edit, name='edit'),
    url(r'^users/(?P<id_num>\d+)$', views.show, name='show'),
    url(r'^users/create$', views.create, name='create'),
    url(r'^users/(?P<id_num>\d+)/destroy$', views.destroy, name='destroy'),
    url(r'^users/update$', views.update, name='update'),

]