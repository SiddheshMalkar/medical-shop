from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add_customer/',views.add_customer,name="add_customer"),
    path('add_medicine/',views.add_medicine,name="add_medicine"),
    path('add_stock/',views.add_stock,name="add_stock"),
]
