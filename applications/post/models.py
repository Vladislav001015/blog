from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Category(models.Model):
    name = models.SlugField(primary_key=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    # image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner.username} {self.post.title}'


class Like(models.Model):
    """
    Модель лайков
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.owner} -> {self.like}'


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ], blank=True, null=True
    )
# post1 **
    def __str__(self):
        return f'{self.owner} -> {self.rating}'