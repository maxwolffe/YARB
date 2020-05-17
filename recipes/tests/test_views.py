from django.contrib.auth.models import User
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse

from recipes.models import Recipe, RecipeBook
from recipes.views import RecipeBookIndexView, RecipeBookDetailView


class TestViews(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username="max", password="123abc")
        self.bookless_user = User.objects.create(
            username="bookless", password="cats")
        self.recipe_book = RecipeBook.objects.create(
            title="Test Recipebook", author="Mr. Magee", owner=self.user)
        self.recipe = Recipe.objects.create(title="Fried chicken",
                                            recipe_book=self.recipe_book)

    def test_signup_get(self):
        client = Client()
        response = client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)

    def test_signup_post(self):
        client = Client()
        response = client.post(reverse('signup'),
                               {'username': 'john',
                                'password1': 'testpassword!',
                                'password2': 'testpassword!'}
                               )
        # If the signup is successful, the user is logged in and directed to the index.
        self.assertEquals(response.url, reverse('index'))
        self.assertEquals(response.status_code, 302)

    def test_recipe_books_index(self):
        request = self.factory.get(reverse('index'))
        request.user = self.user
        response = RecipeBookIndexView.as_view()(request)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(list(response.context_data['recipebook_list']),
                          [self.recipe_book])

    def test_recipe_books_are_empty_if_you_dont_own_any(self):
        request = self.factory.get(reverse('index'))
        request.user = self.bookless_user
        response = RecipeBookIndexView.as_view()(request)
        self.assertEquals(response.status_code, 200)
        # Empty list because the bookless user has no books
        self.assertEquals(list(response.context_data['recipebook_list']),
                          [])

    def test_cant_access_recipe_book_unless_you_own_it(self):
        request = self.factory.get(
            reverse('recipe_detail', args=(self.recipe_book.pk,)))
        request.user = self.bookless_user
        response = RecipeBookDetailView.as_view()(request, pk=self.recipe_book.pk)
        # A 302 is issued to the login page when a member does not have permission to view a resource
        self.assertEquals(response.status_code, 302)

    def test_can_access_recipe_book_if_you_own_it(self):
        request = self.factory.get(
            reverse('recipe_detail', args=(self.recipe_book.pk,)))
        request.user = self.user
        response = RecipeBookDetailView.as_view()(request, pk=self.recipe_book.pk)
        self.assertEquals(response.status_code, 200)
