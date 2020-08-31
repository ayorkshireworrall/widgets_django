from .models import Widget
from .serializers import WidgetSerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, DjangoModelPermissions
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

class WidgetListCreate(generics.ListCreateAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

@api_view(['OPTIONS', 'GET', 'POST'])
def widget_list(request):
    if request.method == 'GET':
        widgets = Widget.objects.all()
        serializer = WidgetSerializer(widgets, many=True)
        response = JsonResponse(serializer.data, safe=False)
        response.__setitem__('Access-Control-Allow-Origin', '*')
        return response
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WidgetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['OPTIONS', 'GET', 'DELETE'])
def widget_detail(request, pk):
    try:
        widget = Widget.objects.get(pk=pk)
    except Widget.DoesNotExist:
        response = HttpResponse(status=404)
        response.__setitem__('Access-Control-Allow-Origin', '*')
        return response

    if request.method == 'OPTIONS':
        response = HttpResponse(status=200)
        response.__setitem__('Access-Control-Allow-Origin', '*')
        response.__setitem__('Access-Control-Allow-Methods', 'OPTIONS, GET, DELETE')
        return response

    
    elif request.method == 'GET':
        serializer = WidgetSerializer(widget)
        response = JsonResponse(serializer.data)
        response.__setitem__('Access-Control-Allow-Origin', '*')
        return response
     
    elif request.method == 'DELETE':
        widget.delete()
        response = HttpResponse(status=204)
        response.__setitem__('Access-Control-Allow-Origin', '*')
        return response

@api_view(['OPTIONS', 'PUT'])
def add_widget(request):
    if request.method == 'OPTIONS':
        response = HttpResponse(status=200)
        response.__setitem__('Access-Control-Allow-Origin', '*')
        response.__setitem__('Access-Control-Allow-Methods', 'OPTIONS, PUT')
        response.__setitem__('Access-Control-Allow-Headers', 'content-type')
        return response

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WidgetSerializer(data=data)
        response = None
        if serializer.is_valid():
            serializer.save()
            response = JsonResponse(serializer.data)
        else:
            response = JsonResponse(serializer.errors, status=400)
        response.__setitem__('Access-Control-Allow-Origin', '*')
        return response
