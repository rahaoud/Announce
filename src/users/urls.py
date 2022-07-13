"""deals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from deals import settings
from users.views import MyUserCreateView, UserProfileCreateView, UserProfileDetailView, UserProfileUpdateView, \
    UserProfileListView, UserProfileDeleteView, MyUserListView, MyUserDetailView, MyUserUpdateView, MyUserDeleteView, \
    IndexListView, login_user, logout_user

urlpatterns = [
    path('', MyUserCreateView.as_view(), name='create-user'),
    path('home', IndexListView.as_view(), name='index_'),
    path('login', login_user, name='user-login'),
    path('logout', logout_user, name='user-logout'),
    path('mm', include('announce.urls')),

    path('list_user', MyUserListView.as_view(), name='index-user'),

    path('detail_user<str:user>/', MyUserDetailView.as_view(), name='detail-user'),
    path('update_user<str:user>/', MyUserUpdateView.as_view(), name='update-user'),
    path('delete_user<str:user>/', MyUserDeleteView.as_view(), name='delete-user'),

    path('list_profile', UserProfileListView.as_view(), name='index-profile'),
    path('create_profile/', UserProfileCreateView.as_view(), name='create-user-profile'),
    path('profile<str:id>/', UserProfileDetailView.as_view(), name='detail-user-profile'),
    path('update_profile<str:id>/', UserProfileUpdateView.as_view(), name='update-user-profile'),
    path('delete_profile<str:id>/', UserProfileDeleteView.as_view(), name='delete-user-profile'),
]
