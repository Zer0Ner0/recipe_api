from django import forms
from .models import Recipe, Ingredient, RecipeStep
from django.forms import inlineformset_factory

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image']  # Update based on your model

IngredientFormSet = inlineformset_factory(
    Recipe, Ingredient,
    fields=['name', 'quantity'],
    extra=1,
    can_delete=True
)

RecipeStepFormSet = inlineformset_factory(
    Recipe, RecipeStep,
    fields=['step_number', 'description'],
    extra=1,
    can_delete=True
)
