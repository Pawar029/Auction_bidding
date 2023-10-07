# usermanagement/urls.py
from django.urls import path
from .views import UserList, UserDetail, UserLogin

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('login/', UserLogin.as_view(), name='user-login'),  # Add this line
]
