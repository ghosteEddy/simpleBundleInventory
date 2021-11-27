from django.urls import path

from . import views

urlpatterns = [
    path('', views.baseIndex, name='baseIndex')
]
