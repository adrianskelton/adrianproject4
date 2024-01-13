from django import forms
from .models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title', 'country', 'featured_image', 'description',
            'ingredients', 'instructions', 'servings'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class DeleteRecipeForm(forms.Form):
    confirmation = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
