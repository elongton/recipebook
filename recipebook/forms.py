from django import forms

from .models import (Unit,
                    Ingredient,
                    Recipe,
                    IngredientSection,
                    IngredientQuantity,)



class AddRecipeForm(forms.ModelForm):
    class Meta():
        model = Recipe
        fields = ('title', 'instructions',)
