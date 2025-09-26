from django.urls.conf import path

from user.views import UserListCreateView , UserUpdateDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('users/register/' , UserListCreateView.as_view(), name="user-register" ),
    path('users/', UserListCreateView.as_view(), name="user-list"),
    path('users/<int:pk>/', UserUpdateDeleteView.as_view(), name="user-details"),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]