from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getproducts/', views.getproducts, name='products'),
    path('productdetail/<int:id>', views.productdetails, name='productdetail'),
]