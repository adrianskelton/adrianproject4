from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Recipe(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    ingredients = models.TextField()
    cooking_instructions = models.TextField()
    
class Meta:
    ordering = ["-created_on"]
    
def __str__(self):
    return self.title