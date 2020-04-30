from django.urls import path

from . import views

urlpatterns = [
    # Recipe Books
    path('', views.RecipeBookIndexView.as_view(), name='index'),
    path('recipe_books', views.RecipeBookIndexView.as_view(), name='index'),
    path('recipe_books/<int:pk>', views.RecipeBookDetailView.as_view(),
         name='recipe_book_detail'),
    path('recipe_books/new', views.RecipeBookCreateView.as_view(),
         name='recipe_book_create'),

    # Recipes
    path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),

    # Meal Lists


    # Accounts
    path('accounts/signup', views.signup, name='signup')
]
