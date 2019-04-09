from django.conf.urls import re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='messenger/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^message/$', views.newMessage, name='newMessage'),
    # re_path(r'^editMessage/$', views.editMessage, name='editMessage'),
    re_path(r'^viewMessage/$', views.viewMessage, name='viewMessage'),
    re_path(r'^home/$', views.home, name='home'),
    path('<int:message_id>/', views.editMessage, name='editMessage'),
]