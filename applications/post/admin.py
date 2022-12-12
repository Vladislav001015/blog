from django.contrib import admin
from applications.post.models import Category, Post, Comment, Like, Rating, Image

class ImageAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 10


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdmin
    ]

admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Rating)