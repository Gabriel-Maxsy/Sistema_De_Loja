from django.core.exceptions import ValidationError
from django import forms
from . import models

class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = (
            'name', 'price', 'description', 'price', 'amount',
        )

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            'name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )
        
        return super().clean()