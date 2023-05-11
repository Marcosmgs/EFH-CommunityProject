from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddRecipeForm(forms.ModelForm):

    class Meta:
        """
        Get recipe model, choose fields to display
        """
        model = Recipe
        fields = ('title', 'prep_time', 'cooking_time', 'description', 'ingredients', 'method', 'featured_image',)
