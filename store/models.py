from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Depois:
# picture (imagem)
# Retirar os campos "blank" e "null" dos Product.owner pois sempre terão donos.

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE, # Se o usuário for excluido, todos os produtos relacionados também serão.
        blank=True, null=True
    )

    def __str__(self):
        
        return f'{self.name} - {self.owner} - {self.category}'
