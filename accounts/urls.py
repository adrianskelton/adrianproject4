from django.urls import path
from .views import login_view, register_view, logout_view, recipe_detail, like_recipe, delete_recipe

app_name = 'accounts'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register')
    path('like_recipe/<int:recipe_id/', like_recipe, name='like_recipe'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail')
    path('delete_recipe/<int:pk>/', delete_recipe, name='delete_recipe'),

]