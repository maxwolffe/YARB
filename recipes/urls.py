from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('recipe_books', views.RecipeBookIndexView.as_view(), name='index'),
    path('recipe_books/<int:pk>', views.RecipeBookDetailView.as_view(),
         name='recipe_book_detail'),
    path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('accounts/signup', views.signup, name='signup')
]
