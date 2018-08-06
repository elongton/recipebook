from django.db import models

# Create your models here.
class Unit(models.Model):
    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=100)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=150)
    instructions = models.TextField(blank=True)
    def __str__(self):
        return self.title



class IngredientSection(models.Model):
    class Meta:
        verbose_name = 'Ingredient Section'
        verbose_name_plural = 'Ingredient Sections'
    section_name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, related_name='ingredient_sections', on_delete = models.CASCADE, null=True)
    def __str__(self):
        return str(self.section_name)




class IngredientQuantity(models.Model):
    class Meta:
        verbose_name = 'Ingredient Quantity'
        verbose_name_plural = 'Ingredient Quantities'
    id = models.AutoField(primary_key = True)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=5, decimal_places=1)
    ingredient_section = models.ForeignKey(IngredientSection, related_name='ingredient_quantities', on_delete = models.CASCADE, null=True)

    def __str__(self):
        return str(self.quantity) + str(' ') + str(self.ingredient)
