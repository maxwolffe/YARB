from django.db import models
from django.contrib.auth.models import User


class RecipeBook(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    recipe_book = models.ForeignKey(RecipeBook, on_delete=models.CASCADE)
    instructions = models.TextField()
    ingredients = models.TextField()

    def __str__(self):
        return self.title


class MealPlan(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe, symmetrical=True)

    def __str__(self):
        return self.title
