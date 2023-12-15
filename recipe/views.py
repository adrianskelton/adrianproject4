from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def recipe_view(request):
    return render(request, 'recipe.html')






