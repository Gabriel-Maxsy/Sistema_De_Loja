from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('<int:product_id>/', views.product, name='product'),
    path('search/', views.search, name='search'), 
    path('', views.index, name='index'),
]