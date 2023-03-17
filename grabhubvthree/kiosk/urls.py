from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('sign_up', views.signup, name='signup'),

    path('customer_list', views.viewcustomerlist, name = 'viewcustomerlist'),
    path('add_customer', views.addcustomer, name = 'addcustomer'),
    path('customer_details/<int:pk>/', views.viewcustomer, name='viewcustomer'),
    path('update_customer_details/<int:pk>/', views.updatecustomer, name = 'updatecustomer'),
    path('delete_customer_details/<int:pk>/', views.deletecustomer, name = 'deletecustomer'),


    path('food_list', views.viewfoodlist, name = 'viewfoodlist'),
    path('add_food', views.addfood, name = 'addfood'),
    path('food_details/<int:pk>/', views.viewfood, name='viewfood'),
    path('update_food_details/<int:pk>/', views.updatefood, name = 'updatefood'),
    path('delete_food_details/<int:pk>/', views.deletefood, name = 'deletefood'),

    path('orders', views.view_orders, name = 'view_orders'),
    path('add_order', views.addorder, name = 'addorder'),
    path('order_details/<int:pk>/', views.order_details, name='order_details'),
    path('update_order_details/<int:pk>/', views.updateorder, name = 'updateorder'),
    path('delete_order_details/<int:pk>/', views.deleteorder, name = 'deleteorder'),


]
