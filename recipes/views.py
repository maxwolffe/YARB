from django.shortcuts import render
from .models import Recipe, RecipeBook, MealPlan
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from guardian.mixins import PermissionRequiredMixin


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class RecipeBookIndexView(LoginRequiredMixin, generic.ListView):
    model = RecipeBook
    template_name = 'recipes/recipebook_index.html'

    def get_queryset(self):
        return RecipeBook.objects.filter(owner=self.request.user)


class RecipeBookDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = RecipeBook
    template_name = 'recipes/recipebook_detail.html'
    permission_required = 'view_recipebook'


class RecipeBookCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = RecipeBook
    fields = ['title', 'author']
    success_url = '/recipe_books'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecipeBookDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = RecipeBook
    success_url = '/recipe_books'


class RecipeBookUpdateView(LoginRequiredMixin, generic.edit.CreateView):
    model = RecipeBook
    fields = ['title', 'author']
    success_url = '/recipe_books'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecipeDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    permission_required = 'view_recipe'
