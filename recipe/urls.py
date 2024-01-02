from django.urls import path
from .views import home, recipe_view, create_recipe, recipe_detail, like_recipe, all_recipes

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/', recipe_view, name='recipe'),
    path('create_recipe/', create_recipe, name='create_recipe'),
    path('like_recipe/<int:pk>/', like_recipe, name='like_recipe'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('all-recipes/', all_recipes, name='all_recipes'),
]