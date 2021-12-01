from django.urls import path

from . import views

urlpatterns = [
    path('', views.baseIndex, name='baseIndex'),
    path('login', views.loginView, name='baseLogin'),
    path('dashboard', views.dashboard, name='baseDashboard'),
    path('logout', views.logoutView, name='baseLogout'),
    path('items', views.itemList, name='baseItemMenu'),
    path('items/delete/<int:item_id>', views.itemDelete, name='baseDeleteItem'),
    path('addItem', views.itemAdd, name='baseAddItem'),
    path('editItem/<int:item_id>', views.itemEdit, name='baseEditItem'),
    path('inventory', views.inventoryMenu, name='baseInventoryMenu'),
]
