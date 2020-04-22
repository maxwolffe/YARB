from django.contrib import admin

from .models import Recipe, RecipeBook, MealPlan

# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeBook)
admin.site.register(MealPlan)
