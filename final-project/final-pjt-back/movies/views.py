from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Movie, Review, Genre
from django.contrib.auth import get_user_model
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer

# Create your views here.
@api_view(['GET'])
def movies(request):
    movie_list = get_list_or_404(Movie)
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def reviews(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        review_list = movie.review_set.all()
        serializer = ReviewSerializer(review_list, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST': # POST
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
   
    elif request.method == 'PUT':
        serializer = ReviewSerializer(reviews, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
    
    else: 
        reviews.delete()
        return Response({'pk': movie_pk})


@api_view(['PUT', 'DELETE'])
def review_update_delete(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  if not request.user.reviews.filter(pk=review_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
    serializer = ReviewSerializer(review, data=request.data)
    
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))
      pre_point = movie.vote_average * (movie.vote_count - 1)
      pre_count = movie.vote_count - 1
      point = pre_point+request.data.get('rank')
      count = movie.vote_count
      new_vote_average = round(point/count, 2)
      movie.vote_average = new_vote_average
      movie.vote_count = count
      movie.save()
      serializer.save(user=request.user)
      return Response(serializer.data)

  else:
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=review.movie_id)
    pre_point = movie.vote_average * (movie.vote_count)
    pre_count = movie.vote_count
    point = pre_point - review.rank
    count = movie.vote_count-1
    new_vote_average = round(point/count, 2)
    movie.vote_average = new_vote_average
    movie.vote_count = count
    movie.save()
    review.delete()
    return Response({ 'id': review_pk })


@api_view(['POST'])
def recommend(request):
    # 인기순
    favorite_movies = Movie.objects.all().order_by('-vote_average')[:10]
   
    favorite_serialize = MovieSerializer(favorite_movies, many=True)
    print(favorite_serialize)
    # 리뷰 기반 장르기반 추천
    user_movies_review = []
    # 좋아요 기반 장르 추천
    user_like_movies = []
    
    # 배우기반 추천
    user_movies_actor = []
    # 감독기반 추천
    user_movies_director = []
    # 개봉년도
    # 제작 국가
    # 연령대
    user_movies_age = []
    # 리뷰 기반 장름별
    reviews = Review.objects.all()
    for review in reviews:
        movie = Movie.objects.get(pk=review.movie_id)
        if not movie in user_movies_review:
            user_movies_review.append(movie)
    
    if user_movies_review:
        serializer = MovieSerializer(user_movies_review[0])
        genre = serializer.data.get('genres')[0]
        genre_name = Genre.objects.get(id=genre)
        idx = 1
        while len(user_movies_review) < 30:
            movie = Movie.objects.get(pk=idx)
            movie_ser = MovieSerializer(movie)
            if movie_ser.data.get('genres')[0] == genre and movie not in user_movies_review:
                user_movies_review.append(movie)
            idx += 1
            # 마지막 데이터
            if idx == 80:
                user_movies_review = Movie.objects.all().order_by('release_date')[:30]
    else:
        user_movies_review = Movie.objects.all().order_by('release_date')[:30]
    
    like_movies = request.data.get('like_movies')
    for like_movies in like_movies:
        movie = get_object_or_404(Movie, pk=like_movies)
        if not movie in user_like_movies:
            user_like_movies.append(movie)

    user_genre_serialize = MovieSerializer(user_movies_review, many=True)
    user_like_serialize = MovieSerializer(user_like_movies, many=True)
    # genre_movies = Movie.objects.all().order_by('-genres')[:10]
    # # 배우별
    # # 감독별
    # # 개봉년도별
    # # 제작 국가별
    # # 연령대
    return Response([favorite_serialize.data, user_genre_serialize.data, user_like_serialize.data])

@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def my_movie_like(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    print(me)
    data = []
    movies = request.data
    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    
    return Response(data)

@api_view(['POST'])
def movie_like(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False
      
  else:
      me.like_movies.add(movie.pk)
      liking = True
  
  return Response(liking)

@api_view(['POST'])
def like_movie_users(request, my_pk):
  # print(request.data)
  users = []
  movies = request.data.get('movies')
  # print(movies)
  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie)
    serializer = MovieSerializer(movie)
    # print(serializer.data)
    for user in serializer.data.get('like_users'):
      if user not in users:
        users.append(user)

  return Response(users)