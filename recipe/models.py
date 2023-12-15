from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Recipe(models.Model):
    """
    My Recipe model to publish recipes
    """
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    servings = models.PositiveIntegerField('servings')
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    
class Meta:
    ordering = ["-created_on"]
    
def __str__(self):
    return self.title