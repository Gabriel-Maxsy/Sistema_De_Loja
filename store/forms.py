# ORGANIZAR ESTE FORMS, DELETAR TESTES DE CODIGOS COMO TESTES DE ERROS E COMENTARIOS.

from django.core.exceptions import ValidationError
from django import forms
from . import models

class ProductForm(forms.ModelForm):

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init',
        # })

    class Meta:
        model = models.Product
        fields = (
            'name', 'price', 'description', 'category', 'amount', 'picture',
        )

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }

    # Se a validação depende de mais de um campo, use clean(self).
    def clean(self):
        cleaned_data = self.cleaned_data
        price = cleaned_data.get('price')
        amount = cleaned_data.get('amount')

        if price == amount:
            msg = ValidationError(
                'Preço não pode ser igual a quantidade',
                code='invalid'
            )

            self.add_error('price', msg)
            self.add_error('amount', msg)
        
        return super().clean()
    
    # Se a validação for específica de um único campo, crie clean_nomeDoCampo().
    def clean_name(self):
       name = self.cleaned_data.get('name')

       if name == 'ABC':
           self.add_error(
               'name',
               ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )
        
       return name