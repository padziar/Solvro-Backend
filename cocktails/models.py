from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_alcoholic = models.BooleanField(default=False)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name