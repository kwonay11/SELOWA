from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movies),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.reviews),

]

