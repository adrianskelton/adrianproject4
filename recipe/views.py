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
    item = get_object_or_404(like_model, pk=pk)

    # Check if user has already liked item 
    if request.user in item.likes.all():
        # User has liked item, so unlike
        item.likes.remove(request.user)
    else:
        # User has not liked, so like
        item.likes.add(request.user)
    # Redirect to recipe detail page
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