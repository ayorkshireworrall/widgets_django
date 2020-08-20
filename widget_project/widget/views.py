from .models import Widget
from .serializers import WidgetSerializer
from rest_framework import generics

class WidgetListCreate(generics.ListCreateAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer