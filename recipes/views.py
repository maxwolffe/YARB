from django.shortcuts import render
from .models import RecipeBook, MealPlan
from django.shortcuts import render

# Create your views here.


def index(request):
    recipes_books = RecipeBook.get(author=user.id)[:5]
    context = {
        'recipes_books': recipes_books,
    }
    return render(request, 'recipes/index.html', context)
