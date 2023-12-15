from django.urls import path
from .views import recipe_view

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/', recipe_view, name='recipe'),
]