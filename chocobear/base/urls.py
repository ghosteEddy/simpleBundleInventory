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
    path('inventory/in', views.inventoryIn, name='baseInventoryIn'),
    path('updateInventory', views.updateInventory, name='baseUpdateInventory'),
    path('inventory/manual', views.inventoryManual, name='baseInventoryManual'),
    path('bundles', views.bundleList, name='baseBundleMenu'),
    path('bundles/add', views.bundleAdd, name='baseBundleAdd'),
    path('inventory/outShopee', views.inventoryOutShopee, name='baseInventoryOutShopee'),
    path('inventory/outLazada', views.inventoryOutLazada, name='baseInventoryOutLazada'),
    path('sellBundle', views.inventorySellBundle, name='baseInventorySellBundle'),
]
