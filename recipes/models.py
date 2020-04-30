from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms


class RecipeBook(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title + " - " + self.author


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
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(MealPlan, self).save(*args, **kwargs)

    def __str__(self):
        return self.title + " " + self.created_at

# Forms
# TODO Move to forms.py


class RecipeBookForm(forms.ModelForm):
    class Meta:
        model = RecipeBook
        fields = ['title', 'author']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'recipe_book', 'instructions', 'ingredients']


class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['owner', 'title', 'recipes']
