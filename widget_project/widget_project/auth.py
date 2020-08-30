from rest_framework_simplejwt import views as jwt_views
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import exception_handler
from rest_framework_simplejwt.authentication import AuthenticationFailed
from rest_framework.parsers import JSONParser

@csrf_exempt
def getTokenPair(request):
    data = JSONParser().parse(request)
    try:
        user = User.objects.get(username=data['username'])
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

def getTokenRefresh():
    response = jwt_views.TokenRefreshView.as_view()
    return response