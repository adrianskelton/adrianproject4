from django import forms 
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'country', 'featured_image', 'description', 'ingredients', 'instructions', 'servings']