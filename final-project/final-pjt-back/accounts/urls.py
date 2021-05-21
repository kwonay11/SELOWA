from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name='accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # 순서 유의!
    path('api-token-auth/', obtain_jwt_token, name='token'),
    # 소셜 로그인
    path('login/kakao/', views.kakao_login, name='kakao_login'),
    path('login/kakao/callback/', views.kakao_callback, name='kakao_login'),


    # path('<username>/', views.profile, name='profile'),
    # path('profile/', views.profile, name='profile'),
]