from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # 순서 유의!
    path('api-token-auth/', obtain_jwt_token, name='token'),
    path('<username>/', views.profile, name='profile'),
]