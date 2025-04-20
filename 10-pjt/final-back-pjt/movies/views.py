from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Actor, Actress, UserProfile, Review 
from .serializers import MovieSerializer, MovieListSerializer, UserProfileSerializer, ActorSerializer, ActressSerializer, ReviewListSerializer, ReviewSerializer
from django.db import transaction

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    serializer = UserProfileSerializer(profile)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_userprofile(request):
    mbti = request.data.get('mbti')
    username = request.data.get('username')
    if mbti and username:
        profile, updated = UserProfile.objects.get_or_create(user=request.user)
        profile.mbti = mbti
        profile.username = username
        profile.save()
        return Response({'status': 'success'})
    else:
        return Response({'status': 'error', 'message': '데이터가 제공되지 않았습니다.'}, status=400)
   
# 영화 조회   
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movies(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

#배우 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def actors(request):
    actors = get_list_or_404(Actor)
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def actresses(request):
    actresses = get_list_or_404(Actress)
    serializer = ActressSerializer(actresses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def actress_detail(request, actress_pk):
    actress = get_object_or_404(Actress, pk=actress_pk)
    serializer = ActressSerializer(actress)
    return Response(serializer.data)


#유저의 프로필을 조회하는 함수
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userprofile(request, user_id):
    userprofile = get_object_or_404(UserProfile, user_id=user_id)
    serializer = UserProfileSerializer(userprofile)
    return Response(serializer.data)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    is_liked = movie.like_users.filter(pk=user.pk).exists()
    is_disliked = movie.dislike_users.filter(pk=user.pk).exists()
    if request.method == 'GET':
        total_likes = movie.like_users.count()
        return Response({
            'is_liked': is_liked,
            'total_likes': total_likes
        }, status=status.HTTP_200_OK)
        
    elif request.method == 'POST':   
        if is_liked:
            movie.like_users.remove(user)
            status_message = 'unliked'
            
        else:
            # 좋아요를 추가하기 전에 싫어요가 되어 있으면 취소
            if is_disliked:
                movie.dislike_users.remove(user)
                
            movie.like_users.add(user)
            status_message = 'liked'
                
        total_likes = movie.like_users.count()
        total_dislikes = movie.dislike_users.count()
        is_liked = movie.like_users.filter(pk=user.pk).exists()
        is_disliked = movie.dislike_users.filter(pk=user.pk).exists()

        return Response({
            'status': status_message,
            'total_likes': total_likes,
            'total_dislikes': total_dislikes,
            'is_liked': is_liked,
            'is_disliked': is_disliked,
            }, status=status.HTTP_200_OK)
                
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def dislikes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    is_disliked = movie.dislike_users.filter(pk=user.pk).exists()
    is_liked = movie.like_users.filter(pk=user.pk).exists()
    if request.method == 'GET':
        total_dislikes = movie.dislike_users.count()
        return Response({
            'is_disliked': is_disliked,
            'total_dislikes': total_dislikes
        }, status=status.HTTP_200_OK)       
    elif request.method == 'POST':   
        if is_disliked:
            movie.dislike_users.remove(user)
            status_message = 'undisliked'     
        else:
            # 싫어요를 추가하기 전에 좋아요가 되어 있으면 취소
            if is_liked:
                movie.like_users.remove(user)               
            movie.dislike_users.add(user)
            status_message = 'disliked'         
        total_dislikes = movie.dislike_users.count()
        total_likes = movie.like_users.count()
        is_liked = movie.like_users.filter(pk=user.pk).exists()
        is_disliked = movie.dislike_users.filter(pk=user.pk).exists()
        return Response({
            'status': status_message,
            'total_dislikes': total_dislikes,
            'total_likes': total_likes,
            'is_disliked': is_disliked,
            'is_liked': is_liked,
            }, status=status.HTTP_200_OK)

# 댓글관련 view
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def reviews(request, movie_pk):
    reviews = Review.objects.filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk, movie=movie)
    serializer = ReviewListSerializer(review)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    user = request.user
    content = request.data.get('content')
    partner_mbti = request.data.get('partner_mbti')
    # UserProfile에서 MBTI 가져오기
    profile, created = UserProfile.objects.get_or_create(user=user)
    # 영화 객체 가져오기
    movie = get_object_or_404(Movie, pk=movie_pk)
    like_review = request.data.get('like_review', False)
    dislike_review = request.data.get('dislike_review', False)
    # 리뷰 생성
    review = Review.objects.create(
        user=user,
        user_mbti=profile.mbti,
        partner_mbti=partner_mbti,
        movie=movie,
        movie_title=movie.title,
        content=content,
        like_review=like_review,
        dislike_review=dislike_review,
    )
    return Response({'status': 'success', 'review_id': review.id})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_review(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk, user=request.user, movie=movie)
    data = request.data.copy()
    data['movie_title'] = movie.title
    data['movie'] = movie_pk
    serializer = ReviewSerializer(instance=review, data=data, partial=True, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_review(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk, user=request.user, movie=movie)
    review.delete()
    return Response({"detail": "리뷰가 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
    
# @require_POST
# def create_comment(request, review_pk):
#     review = Review.objects.get(pk=review_pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.review = review
#         comment.user = request.user
#         comment.save()
#         return redirect('community:detail', review.pk)
#     context = {
#         'comment_form': comment_form,
#         'review': review,
#         'comments': review.comment_set.all(),
#     }
#     return render(request, 'community/detail.html', context)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def like(request, review_pk):
#     review = Review.objects.get(pk=review_pk)
#     if request.user in review.like_users.all():
#         review.like_users.remove(request.user)
#         is_liked = False
#     else:
#         review.like_users.add(request.user)
#         is_liked = True 
#     context = {
#         'is_liked':is_liked,
#         'like_count':review.like_users.count(),
#     }
#     return JsonResponse(context)