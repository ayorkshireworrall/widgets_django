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
        response.__setitem__('Access-Control-Allow-Credentials', 'true')
        response.__setitem__('set-cookie', 'AWSALBCORS=f6FHXY7nV+RZH8mMfrFZ/ltICa3rLz+1z8ZGpzQEcBVjfTQiAjXofxb5MAZp1voeDz7+QG3ts6e/DgbuKiJCZnOI/d6YTKDhecdI4hEXwcAgIQO0Ey4iGA4dm0eo; Expires=Sun, 06 Sep 2020 08:55:51 GMT; Path=/; SameSite=None;')
        response.set_cookie('REFRESH_TOKEN', refreshToken, httponly=True, samesite='None', max_age=1000000, domain='api.app.localhost')
        return response
    except (User.DoesNotExist, AuthenticationFailed) as e:
        response = JsonResponse({'detail':'Authentication failed, check username and password'}, status=403)
        return response

def getTokenRefresh():
    response = jwt_views.TokenRefreshView.as_view()
    return response