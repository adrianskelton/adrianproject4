from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Recipe(models.Model):
    """
    My Recipe model to publish recipes
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.PositiveIntegerField(validators=[MaxValueValidator(20)])
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ["-date"]
        
    def __str__(self):
        return self.title

class like_model(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_recipes')
    dislikes = models.ManyToManyField(User, related_name='disliked_recipes')

    def __str__(self):
        return f"{self.title} - Likes: {self.likes.count()}, Dislikes: {self.dislikes.count()}"