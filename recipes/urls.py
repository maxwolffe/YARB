from django.urls import path

from . import views

urlpatterns = [
    # Recipe Books
    path('', views.RecipeBookIndexView.as_view(), name='index'),
    path('recipe_books', views.RecipeBookIndexView.as_view(), name='index'),
    path('recipe_books/<int:pk>', views.RecipeBookDetailView.as_view(),
         name='recipe_book_detail'),
    path('recipe_books/<int:pk>/update', views.RecipeBookUpdateView.as_view(),
         name='recipe_book_update'),
    path('recipe_books/<int:pk>/delete', views.RecipeBookDeleteView.as_view(),
         name='recipe_book_delete'),
    path('recipe_books/new', views.RecipeBookCreateView.as_view(),
         name='recipe_book_create'),

    # Recipes
    path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/new', views.RecipeCreateView.as_view(),
         name='recipe_create'),
    path('recipes/<int:pk>/update', views.RecipeUpdateView.as_view(),
         name='recipe_update'),
    path('recipes/<int:pk>/delete', views.RecipeDeleteView.as_view(),
         name='recipe_delete'),
    # Meal Lists


    # Accounts
    path('accounts/signup', views.signup, name='signup')
]
