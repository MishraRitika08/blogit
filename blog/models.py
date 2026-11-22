from django.db import models
from django.contrib.auth.models import User


# related_name='posts' lets you access all posts written by a user.
''' 
user = User.objects.get(username='ritika')
user.posts.all() 
'''
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length = 200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['author', '-created_at']),
        ]
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = 'comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class AIGenerationHistory(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'ai_generation_history')
    post = models.ForeignKey(Post, on_delete = models.SET_NULL, null=True, blank = True, related_name = 'ai_generations')
    prompt = models.TextField()
    generated_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'AI Generation by {self.user.username} at {self.created_at}'    

'''
-- View all tables
\dt

-- View auth_user structure
\d auth_user

'''
