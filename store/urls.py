from django.urls import path
from store import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'), 

    # Product CRUD 
    path('product/<int:product_id>/', views.product, name='product'), # Read
    path('product/create/', views.create, name='create'), # Create
    path('product/<int:product_id>/update/', views.update, name='update'), # Update
    path('product/<int:product_id>/delete/', views.delete, name='delete'), # Delete
]