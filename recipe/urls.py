from . import views
from django.urls import path
from .views import home, recipe_view, create_or_edit_recipe, recipe_detail, user_recipes, like_recipe, unlike_recipe, top_five, sort_by_country, latest_recipes, all_recipes, add_comment, delete_recipe


urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/', recipe_view, name='recipe'),
    path('create-recipe/', create_or_edit_recipe, name='create_recipe'),
    path('edit-recipe/<int:pk>/', create_or_edit_recipe, name='edit_recipe'),
    path('like_recipe/<int:pk>/', like_recipe, name='like_recipe'),
    path('unlike_recipe/<int:pk>/', unlike_recipe, name='unlike_recipe'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('all-recipes/', all_recipes, name='all_recipes'),
    path('top_five/', top_five.as_view(), name='top_five'),
    path('latest-recipes/', latest_recipes, name='latest_recipes'),
    path('sort-by-country/', sort_by_country, name='sort_by_country'),
    path('user-recipes/', user_recipes, name='user_recipes'),
    path('recipe/<int:recipe_id>/add_comment/', add_comment, name='add_comment'),
    path('delete_recipe/<int:pk>/', delete_recipe, name='delete_recipe'),
]
