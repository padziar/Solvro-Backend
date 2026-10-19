from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_alcoholic = models.BooleanField(default=False)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Cocktail(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name} w {self.cocktail.name}"