from django.contrib.auth.models import User
from django.test import TestCase
from recipes.forms import RecipeModelForm
from recipes.models import Recipe, RecipeBook


class TestForms(TestCase):

    def setUp(self):
        owner = User.objects.create(username="max", password="123abc")
        recipe_book = RecipeBook.objects.create(
            title="Test Recipebook", author="Mr. Magee", owner=owner)
        recipe = Recipe.objects.create(
            title="Fried chicken", recipe_book=recipe_book)
        pass

    def test_recipe_form_recipe_book_choices_limited_to_owned_books(self):
        user = User.objects.get(username="max")
        form = RecipeModelForm(user=user)
        self.assertEqual(
            list(form.fields['recipe_book'].queryset), list(RecipeBook.objects.filter(owner=user)))

    def test_recipe_form_valid_data(self):
        form = RecipeModelForm(
            user=User.objects.get(username="max"),
            data={
                'title': "Fill'er up chicken",
                'recipe_book': RecipeBook.objects.get(title="Test Recipebook"),
                'instructions': "asdf",
                'ingredients': "asdf"
            }
        )
        self.assertTrue(form.is_valid())

    def test_recipe_form_invalid_when_adding_to_recipe_book_user_does_not_own(self):
        form = RecipeModelForm(
            user=User.objects.create(username="imposter"),
            data={
                'title': "Fill'er up chicken",
                'instructions': "asdf",
                'ingredients': "asdf"
            }
        )
        self.assertFalse(form.is_valid())
