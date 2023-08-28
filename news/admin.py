from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'ratingAuthor')


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('postThrough', 'categoryThrough')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentPost', 'commentUser', 'text', 'dateCreation', 'rating')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)


#admin.site.register(Order)
# Register your models here.
