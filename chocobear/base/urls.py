from django.urls import path

from . import views

urlpatterns = [
    path('', views.baseIndex, name='baseIndex'),
    path('login', views.loginView, name='baseLogin'),
    path('dashboard', views.dashboard, name='baseDashboard'),
    path('logout', views.logoutView, name='baseLogout')
]
