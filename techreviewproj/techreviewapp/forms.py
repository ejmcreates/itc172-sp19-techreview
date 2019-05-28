from django import forms
from .models import Product, Review, TechType

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'        

        