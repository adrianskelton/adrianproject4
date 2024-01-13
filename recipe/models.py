from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator


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
    likes = models.ManyToManyField(User, related_name='recipe_likes',
                                   blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title


class Like_model(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_recipes')
    dislikes = models.ManyToManyField(User, related_name='disliked_recipes')

    def __str__(self):
        return f"{self.title} - Likes: {self.likes.count()},"
        f"Dislikes: {self.dislikes.count()}"


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    body = models.TextField()
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             related_name='comments')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(null=True)

    def __str__(self):
        return f"Comment from {self.name} on {self.post}"
