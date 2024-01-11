from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe

class RecipeDetailViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test recipe
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            country='Test Country',
            featured_image='test_image.jpg',  # Provide a path to a test image or use Cloudinary mock data
            description='This is a test recipe.',
            ingredients='Ingredient 1, Ingredient 2',
            instructions='Step 1, Step 2',
            servings=4,
            author=self.user,
        )

    def test_recipe_detail_view(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Get the URL for the recipe detail view
        url = reverse('recipe_detail', args=[str(self.recipe.id)])

        # Issue a GET request to the URL
        response = self.client.get(url)

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the recipe title
        self.assertContains(response, 'Test Recipe')

        # Check that the response contains the recipe author's username
        self.assertContains(response, 'testuser')

        # Check that the response contains the recipe description
        self.assertContains(response, 'This is a test recipe.')

