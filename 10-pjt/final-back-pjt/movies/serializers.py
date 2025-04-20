from rest_framework import serializers
from .models import Movie, UserProfile, Actor, Actress, Review
from django.contrib.auth import get_user_model



class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'mbti', 'username']

class ActressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actress
        fields = '__all__'
        
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

# 댓글관련 serializers
class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    user_mbti = serializers.CharField(source='user.userprofile.mbti', read_only=True)

    class Meta:
        model = Review
        fields = ['id','movie_title', 'content', 'movie', 'user' ,'username', 'user_mbti','partner_mbti' ,'created_at', 'updated_at', 'like_review', 'dislike_review']
        read_only_fields = ['user']

class ReviewSerializer(serializers.ModelSerializer): 
    username = serializers.CharField(source='user.username', read_only=True)
    user_mbti = serializers.CharField(source='userprofile.mbti', read_only=True)
    class Meta:
        model = Review
        fields = ['id','movie_title', 'content', 'movie', 'user' ,'username', 'user_mbti', 'partner_mbti' ,'created_at', 'updated_at', 'like_review', 'dislike_review']
        read_only_fields = ['user']