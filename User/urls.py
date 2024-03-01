from .views import home, RegistrationView, CustomLoginView, UserList, UserProfile
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('userlist/', UserList.as_view(), name='userlist'),
    path('userprofile/', UserProfile.as_view(), name='userprofile'),
]
