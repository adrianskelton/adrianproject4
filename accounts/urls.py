from django.urls import path
from .views import login_view, register_view, logout_view, recipe_detail

app_name = 'accounts'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register')
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail')
]