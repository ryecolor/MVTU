from django.db import models
from django.conf import settings
from accounts.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Movie(models.Model):
    
    title = models.CharField(max_length=255)
    released = models.IntegerField()
    category = models.CharField(max_length=100)
    running_time = models.CharField(max_length=50)
    poster_url = models.URLField()
    detail = models.TextField()
    score = models.FloatField()
    trailer_url = models.URLField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movies')
    
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.like_users.count()
        
            
class Actor(models.Model):
    movie =models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mbti = models.CharField(max_length=4)
    detail = models.TextField()
    img = models.URLField()
    
class Actress(models.Model):
    movie =models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mbti = models.CharField(max_length=4)
    detail = models.TextField()
    img = models.URLField()
    

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mbti = models.CharField(max_length=4)
    username = models.CharField(max_length=30)
    
    
class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    user_mbti = models.CharField(max_length=4)
    partner_mbti = models.CharField(max_length=4)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_review = models.BooleanField(default=False)
    dislike_review = models.BooleanField(default=False)
    # like_users = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, related_name='like_reviews'
    # )
    # dislike_users = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, related_name='like_reviews'
    # )
    def get_user_mbti(self):
        return self.user.userprofile.mbti

    def __str__(self):
        return f"{self.movie_title} - {self.title} by {self.get_username()}"    