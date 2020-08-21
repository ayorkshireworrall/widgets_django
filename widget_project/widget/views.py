from .models import Widget
from .serializers import WidgetSerializer
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

class WidgetListCreate(generics.ListCreateAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

#TODO remove exemption when authentication in place
@csrf_exempt
def widget_list(request):
    if request.method == 'GET':
        widgets = Widget.objects.all()
        serializer = WidgetSerializer(widgets, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WidgetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#TODO remove exemption when authentication in place
@csrf_exempt
def widget_detail(request, pk):
    try:
        widget = Widget.objects.get(pk=pk)
    except Widget.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = WidgetSerializer(widget)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WidgetSerializer(widget, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
     
    elif request.method == 'DELETE':
        widget.delete()
        return HttpResponse(status=204)
