from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'), 

    # Product CRUD 
    path('<int:product_id>/', views.product, name='product'),
]