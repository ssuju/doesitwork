from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'rhymesapp'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('audio_list', views.audio_list, name='audio_list'),
    path('account_information', views.account_information, name='account_information'),
    path('nurseryList', views.nurseryList, name='nurseryList'),
    path('nurseryPage', views.nurseryPage, name='nurseryPage'),
    path('signup', views.signup, name='signup'),
    path('upgrade', views.upgrade, name='upgrade'),

]


