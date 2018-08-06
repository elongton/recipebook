from django.contrib import admin
from .models import Ingredient, Unit, IngredientQuantity, IngredientSection, Recipe
# Register your models here.
admin.site.register(Recipe)
admin.site.register(IngredientSection)
admin.site.register(Ingredient)
admin.site.register(Unit)

class IngredientQuantityAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'quantity', 'unit')
    def unit(self, obj):
        return obj.ingredient.unit

admin.site.register(IngredientQuantity, IngredientQuantityAdmin)
