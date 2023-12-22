from django.urls import path
from .views import home, recipe_view, create_recipe, recipe_detail

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/', recipe_view, name='recipe'),
    path('create_recipe/', recipe_view, name='create_recipe'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
]