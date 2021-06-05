from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movies),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.reviews),
    path('review/<int:review_pk>/', views.review_update_delete),
    path('review/<int:my_pk>', views.my_review),
    path('recommend/', views.recommend),
    path('<int:my_pk>/<movie_title>/like/', views.movie_like),
    path('<int:my_pk>/like/', views.my_movie_like),
    path('<int:my_pk>/like/users/', views.like_movie_users)
]

