from django.urls import path
from . import views


urlpatterns = [
    #유저 프로필 조회
    path('get-profile/', views.get_profile, name='get_profile'),
    #기본 프로필정보 생성
    # path('create-userprofile/', views.create_userprofile, name='create_userprofile'),
    #프로필정보 수정
    path('update-userprofile/', views.update_userprofile, name='update_userprofile'),
    
    #영화 조회
    path('movies/', views.movies, name='movies'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_pk>/likes/', views.likes, name='likes'),
    path('movies/<int:movie_pk>/dislikes/', views.dislikes, name='dislikes'),
    
    #배우 조회
    path('actors/', views.actors, name='actors'),
    path('actors/<int:actor_pk>/', views.actor_detail, name='actor_detail'),
    path('actresses/', views.actresses, name='actresses'),
    path('actresses/<int:actress_pk>/', views.actress_detail, name='actress_detail'),
    
    #프로필 조회
    path('userprofile/<int:user_id>/', views.userprofile, name='userprofile'),

    # 댓글 관련
    path('movies/<int:movie_pk>/reviews/', views.reviews, name='reviews'),
    path('movies/<int:movie_pk>/create_review/', views.create_review, name='create_review'),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/update_review/', views.update_review, name='update_review'),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/delete_review/', views.delete_review, name='delete_review'),
    # path('<int:review_pk>/like/', views.like, name='like'),
]