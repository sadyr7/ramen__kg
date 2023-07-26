from django.db import models
from post.models import Post
# Create your models here.
class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey('CustomUser', related_name='likes', on_delete=models.CASCADE)

class Favorite(models.Model):
    user = models.ForeignKey('CustomUser', related_name='favorites', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='favorites', on_delete=models.CASCADE)