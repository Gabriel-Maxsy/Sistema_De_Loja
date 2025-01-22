import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice, randint

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_PRODUCTS = 40  # Número de produtos a serem criados

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    from store.models import Category, Product

    # Limpa os dados existentes
    Product.objects.all().delete()
    Category.objects.all().delete()

    # Categorias e produtos reais
    categories_with_products = {
        "Ferramentas": [
            "Martelo", "Alicate", "Chave de Fenda", "Furadeira", "Serrote",
            "Parafusadeira", "Marreta", "Trena", "Esquadro", "Lixa"
        ],
        "Elétrica": [
            "Interruptor", "Tomada", "Fio Elétrico", "Lâmpada LED", "Transformador",
            "Fusível", "Disjuntor", "Reator", "Sensor de Presença", "Extensão"
        ],
        "Tintas": [
            "Tinta Acrílica", "Tinta Spray", "Tinta à Óleo", "Rolo de Pintura",
            "Pincel", "Removedor de Tinta", "Selador", "Massa Corrida",
            "Balde de Tinta", "Colorante"
        ],
        "Eletrônicos": [
            "Celular", "Carregador Portátil", "Fone de Ouvido", "Mouse",
            "Teclado", "Monitor", "Smartwatch", "Caixa de Som Bluetooth",
            "Notebook", "Câmera de Segurança"
        ],
        "Livros": [
            "O Senhor dos Anéis", "Dom Casmurro", "A Revolução dos Bichos",
            "1984", "Harry Potter", "O Pequeno Príncipe", "Os Miseráveis",
            "Orgulho e Preconceito", "Moby Dick", "Capitães da Areia"
        ],
    }

    # Cria categorias
    categories = []
    for category_name in categories_with_products.keys():
        category = Category(name=category_name)
        category.save()
        categories.append((category, categories_with_products[category_name]))

    # Cria produtos
    products = []
    for _ in range(NUMBER_OF_PRODUCTS):
        # Seleciona uma categoria aleatória
        category, product_names = choice(categories)
        name = choice(product_names)  # Seleciona um produto da categoria
        description = f"Descrição detalhada do produto {name.lower()}."
        price = round(randint(10, 500) + randint(0, 99) / 100, 2)  # Preço entre R$10 e R$500
        amount = randint(1, 100)  # Estoque de 1 a 100 unidades
        created_date = datetime.now()

        products.append(
            Product(
                name=name,
                description=description,
                price=price,
                amount=amount,
                created_date=created_date,
                category=category,
            )
        )

    # Salva todos os produtos no banco de dados
    if products:
        Product.objects.bulk_create(products)

    print(f'{NUMBER_OF_PRODUCTS} produtos criados com sucesso!')
