from django.urls import path
from .views import getTokenPair, getTokenRefresh, logout

urlpatterns = [
    path('api/token/', getTokenPair, name='token_obtain_pair'),
    path('api/token/refresh/', getTokenRefresh, name='token_refresh'),
    path('api/logout', logout, name='logout'),
]