from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.views import generic, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import CommentForm, AddRecipeForm


class RecipeList(generic.ListView):
    """
    This view is used to display paginated by 6 all recipes in the index page
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetails(View):
    """
    This view is used to display recipe details including comments filter likes.
    It also includes the comment form and add to meal plan form
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Retrive recipe and related comments and likes from the database
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Method called when a POST request is made to the view
        in the comment form.
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RecipeLike(View):

    def post(self, request, slug):
        """
        Method called when a POST request is made to the view
        via the like option.
        """
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))


class AddRecipe(generic.CreateView):
    """
    View used to allow logged in users to create recipes
    """
    model = Recipe
    template_name = 'add_recipe.html'
    form_class = AddRecipeForm
    success_url = reverse_lazy("my_book")

    def form_valid(self, form):
        """
        Method called when valid form data has been posted.
        Signed user set as the author of the recipe.
        set success message given to display
        """
        form.instance.author = self.request.user
        messages.success(self.request, "Recipe Added successfully")
        return super().form_valid(form)


class MyRecipeBook(generic.ListView):
    """
    View used to allow logged in users view a list of own created recipes
    """
    model = Recipe
    queryset = Recipe.objects.order_by('created_on')
    template_name = 'my_book.html'
    paginate_by = 6

    def get_queryset(self):
        """
        Override get_queryset to filter by user
        """
        return Recipe.objects.filter(author=self.request.user)


class SingleRecipe(View):
    """
    View used to allow logged in users to view recipes
    details for each one created
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Override get_queryset to filter by status 0
        Get object recipe by slug field
        """
        queryset = Recipe.objects.filter(status=0)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "single_recipe.html",
            {
                "recipe": recipe,
            },
        )


class UpdateRecipe(generic.UpdateView):
    """
    View used to allow logged in users update already created recipes
    """
    model = Recipe
    template_name = 'edit_recipe.html'
    form_class = AddRecipeForm
    success_url = reverse_lazy("my_book")

    def form_valid(self, form):
        """
        Method called when valid form data has been posted.
        Signed user set as the author of the recipe.
        """
        form.instance.author = self.request.user
        messages.success(self.request, "Recipe updated successfully")
        return super().form_valid(form)


class DeleteRecipe(generic.DeleteView):
    """
    View used to allow logged in users delete created recipes
    """
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy("my_book")

    def delete(self, request, *args, **kwargs):
        """
        This function is used to display sucess message given
        """
        messages.success(self.request, "Recipe deleted successfully")
        return super(DeleteRecipe, self).delete(request, *args, **kwargs)
