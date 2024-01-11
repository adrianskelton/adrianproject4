from django.contrib import admin
from .models import Recipe, Comment, Like_model

admin.site.register(Recipe)
admin.site.register(Like_model)  



class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ('status',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'email')
    date_hierarchy = 'created'

