from django.shortcuts import render
from .models import Recipe, RecipeBook, MealPlan
from .forms import RecipeModelForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_list'] = self.object.recipe_set.all()
        return context


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


class RecipeBookUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
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


class RecipeCreateView(generic.CreateView, LoginRequiredMixin):
    template_name = 'recipes/recipe_form.html'

    def get(self, request, *args, **kwargs):
        form = RecipeModelForm(user=request.user)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RecipeModelForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
        context = {"form": form}
        return render(request, self.template_name, context)


class RecipeUpdateView(generic.UpdateView, PermissionRequiredMixin, LoginRequiredMixin):
    template_name = 'recipes/recipe_form.html'
    permission_required = 'view_recipe'

    def get(self, request, *args, **kwargs):
        recipe = get_object_or_404(Recipe, pk=self.kwargs['pk'])
        form = RecipeModelForm(instance=recipe, user=request.user)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RecipeModelForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
        context = {"form": form}
        return render(request, self.template_name, context)


class RecipeDeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Recipe
    success_url = '/recipe_books'
