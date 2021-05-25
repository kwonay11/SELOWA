from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Movie, Review
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

@api_view(['GET', 'POST'])
def reviews(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        review_list = movie.review_set.all()
        serializer = ReviewSerializer(review_list, many=True)
        return Response(serializer.data)
    else: # POST
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def recommend(request):
    # 인기순
    favorite_movies = Movie.objects.all().order_by('-vote_average')[:10]
   
    serializer1 = MovieSerializer(favorite_movies, many=True)
    # 리뷰 기반 장르기반 추천
    user_movies_review = []
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
        idx = 1
        while len(user_movies_review) < 30:
            movie = Movie.objects.get(pk=idx)
            movie_ser = MovieSerializer(movie)
            # print(movie)
            if movie_ser.data.get('genres')[0] == genre and movie not in user_movies_review:
                user_movies_review.append(movie)
            idx += 1
            if idx == 75:
                user_movies_review = Movie.objects.all().order_by('release_date')[:30]
    else:
        user_movies_review = Movie.objects.all().order_by('release_date')[:30]
    print(user_movies_review)
    
    # genre_movies = Movie.objects.all().order_by('-genres')[:10]
    # # 배우별
    # # 감독별
    # # 개봉년도별
    # # 제작 국가별
    # # 연령대
    return Response(user_movies_review)

@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def my_movie_like(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    data = []
    movies = request.data
    for movie_pk in movies:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        data.append(serializer.data)
    
    return Response(data)