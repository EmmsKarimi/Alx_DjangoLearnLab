from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', through='UserFollower', blank=True)

    def __str__(self):
        return self.username

class UserFollower(models.Model):
    user = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, related_name='followed_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'followed_user')

    def __str__(self):
        return f"{self.user} follows {self.followed_user}"
