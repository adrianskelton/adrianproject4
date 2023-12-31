from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from django import forms
from .forms import RecipeForm, CommentForm, DeleteRecipeForm
from .models import Recipe, like_model, Comment


@login_required
def create_or_edit_recipe(request, pk=None):
    # If 'pk' is provided, it's an edit operation, otherwise, it's a create operation
    if pk:
        recipe = get_object_or_404(Recipe, pk=pk)
    else:
        recipe = None

    form = RecipeForm(instance=recipe)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect("recipe_detail", pk=recipe.pk)

    return render(request, "create_recipe.html", {"form": form})



def like_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    # Check if user has already liked item
    if request.user in recipe.likes.all():
        # User has liked item, so unlike
        recipe.likes.remove(request.user)
    else:
        # User has not liked, so like
        recipe.likes.add(request.user)
    # Redirect to recipe detail page
    return redirect("recipe_detail", pk=pk)


def unlike_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    # Check if the user has already liked the recipe
    if request.user in recipe.likes.all():
        # User has liked the recipe, so unlike
        recipe.likes.remove(request.user)

    # Redirect to the recipe detail page
    return redirect("recipe_detail", pk=pk)


def home(request):
    # return render(request, 'index.html')

    latest_recipes = Recipe.objects.order_by("-date")[:5]

    context = {
        "new_section_data": latest_recipes,
    }

    return render(request, "index.html", context)


def recipe_view(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe.html", {"Recipes": recipes})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = recipe.comments.all()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.recipe = recipe
            new_comment.save()

    return render(
        request,
        "recipe_detail.html",
        {"recipe": recipe, "comments": comments, "comment_form": comment_form},
    )


def all_recipes(request):
    all_recipes_list = Recipe.objects.all()
    paginator = Paginator(all_recipes_list, 10)  # Show 10 recipes per page

    page = request.GET.get("page")
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        recipes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        recipes = paginator.page(paginator.num_pages)

    return render(request, "all_recipes.html", {"recipes": recipes})


def user_recipes(request):
    user_recipes = Recipe.objects.filter(author=request.user)
    return render(request, "user_recipes.html", {"user_recipes": user_recipes})


class top_five(View):
    template_name = 'top_five.html'
    def get(self, request, *args, **kwargs):
        top_five_recipes = Recipe.objects.order_by('-likes__count')[:5]
        return render(request, self.template_name, {'recipes': top_five_recipes})


def sort_by_country(request, country):
    recipes_by_country = Recipe.objects.filter(country=country)
    return render(request, "recipes_by_country.html", {"recipes": recipes_by_country})


def latest_recipes(request):
    latest_recipes = Recipe.objects.order_by("-created_at")[:5]
    return render(request, "latest_recipes.html", {"recipes": latest_recipes})


def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = recipe
            new_comment.save()

            return redirect("recipe_detail", pk=recipe_id)

    else:
        form = CommentForm()

    return render(request, "recipe/add_comment.html", {"form": form})


def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("user_recipes")  # Redirect to the user_recipes page after editing
    else:
        form = RecipeForm(instance=recipe)

    return render(request, "edit_recipe.html", {"form": form, "recipe": recipe})


def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = DeleteRecipeForm(request.POST)
        if form.is_valid() and form.cleaned_data["confirmation"]:
            recipe.delete()
            return redirect("user_recipes")
    else:
        form = DeleteRecipeForm()

    return render(request, "delete_recipe.html", {"recipe": recipe, "form": form})
