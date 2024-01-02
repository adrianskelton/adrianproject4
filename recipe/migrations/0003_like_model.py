# Generated by Django 3.2.23 on 2023-12-23 15:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0002_remove_recipe_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='like_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('dislikes', models.ManyToManyField(related_name='disliked_recipes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='liked_recipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]