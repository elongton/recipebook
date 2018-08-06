from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Recipe
from .forms import AddRecipeForm

class RecipeList(ListView):
    model = Recipe
    context_object_name = 'recipes'


class AddRecipeView(FormView):
    template_name = 'recipebook/add_recipe.html'
    form_class = AddRecipeForm
    success_url = '/'
