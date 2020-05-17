from django import forms

from .models import Recipe, RecipeBook


class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'recipe_book', 'instructions', 'ingredients']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(RecipeModelForm, self).__init__(*args, **kwargs)

        self.fields['recipe_book'].queryset = RecipeBook.objects.filter(
            owner=self.user)

    def clean_recipe_book(self):
        recipe_book = self.cleaned_data.get('recipe_book')
        if recipe_book.owner != self.user:
            raise forms.ValidationError(
                "You cannot add recipes to books you do not own.")
        return recipe_book
