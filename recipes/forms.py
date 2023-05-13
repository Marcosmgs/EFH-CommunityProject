from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form created to add commets to database
    Get recipe model and choose fields to display
    """
    class Meta:
        model = Comment
        fields = ('body',)


class AddRecipeForm(forms.ModelForm):

    class Meta:
        """
        Form created to add and update recipes to database
        Get recipe model and choose fields to display
        """
        model = Recipe
        fields = ('title', 'prep_time', 'cooking_time', 'description', 'ingredients', 'method', 'featured_image',)
