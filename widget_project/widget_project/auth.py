from rest_framework_simplejwt import views as jwt_views
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import exception_handler
from rest_framework_simplejwt.authentication import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.parsers import JSONParser

@csrf_exempt
def getTokenPair(request):
    data = JSONParser().parse(request)
    try:
        user = User.objects.get(Q(username=data['username']) | Q(email=data['username']))
        isValidPass = user.check_password(data['password'])
        if not isValidPass:
            raise AuthenticationFailed()
        refreshToken = RefreshToken.for_user(user)
        response = JsonResponse({
            'access': str(refreshToken.access_token)
        })
        response.set_cookie('REFRESH_TOKEN', refreshToken, httponly=True, max_age=3600)
        return response
    except (User.DoesNotExist, AuthenticationFailed) as e:
        response = JsonResponse({'detail':'Authentication failed, check username and password'}, status=403)
        return response

@csrf_exempt
def getTokenRefresh(request):
    try:
        cookie_token = request.COOKIES.get('REFRESH_TOKEN')
        #A random new token generated if None passed in!! (No user assigned so lacks permissions but still annoying)
        if cookie_token is None:
            cookie_token = 0
        refresh_token = RefreshToken(cookie_token)
        response = JsonResponse({
            'access': str(refresh_token.access_token)
        })
        return response
    except TokenError as e:
        response = JsonResponse({'detail':'Invalid or expired refresh token provided'}, status=403)
        return response

def logout(request):
    try:
        response = JsonResponse({})
        response.delete_cookie('REFRESH_TOKEN')
        return response
        #TODO need to learn how to handle errors properly, wtf is this hack?
    except TokenError as e:
        response = JsonResponse({'detail': 'Error logging out'}, status=500)
        return response
    