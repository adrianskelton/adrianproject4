from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .forms import RecipeForm
from .models import Recipe  # Import the Recipe model
from .models import like_model

def create_recipe(request):
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail', pk=recipe.pk)

    print(form.errors)  # Add this line to print form errors in the terminal
    return render(request, 'create_recipe.html', {'form': form})

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
    return redirect('recipe_detail', pk=pk) 

def unlike_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    # Check if the user has already liked the recipe
    if request.user in recipe.likes.all():
        # User has liked the recipe, so unlike
        recipe.likes.remove(request.user)

    # Redirect to the recipe detail page
    return redirect('recipe_detail', pk=pk)

def home(request):
    #return render(request, 'index.html')

    latest_recipes = Recipe.objects.order_by('-date')[:5]

    context = {
        'new_section_data': latest_recipes,
        # Include other context variables as needed
    }

    return render(request, 'index.html', context)

def recipe_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe.html', {'Recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def all_recipes(request):
    all_recipes_list = Recipe.objects.all()
    paginator = Paginator(all_recipes_list, 10) #Show 10 recipes per page

    page = request.GET.get('page')
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        recipes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        recipes = paginator.page(paginator.num_pages)

    return render(request, 'all_recipes.html', {'recipes': recipes})

def top_five(request):
    top_five_recipes = Recipe.objects.order_by('-likes__count')[:5]
    return render(request, 'top_five.html', {'recipes': top_five_recipes})

def sort_by_country(request, country):
    recipes_by_country = Recipe.objects.filter(country=country)
    return render(request, 'recipes_by_country.html', {'recipes': recipes_by_country})

def latest_recipes(request):
    latest_recipes = Recipe.objects.order_by('-created_at')[:5]
    return render(request, 'latest_recipes.html', {'recipes': latest_recipes})

def user_recipes(request):
    user_recipes = Recipe.objects.filter(author=request.user)
    return render(request, 'user_recipes.html', {'user_recipes': user_recipes})

def get_default_author():
    return User.objects.get(username='default_username')

    author = models.ForeignKey(User, on_delete=models.CASCADE)