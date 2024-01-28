from django.urls import path
from products import views

urlpatterns = [
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

]
