from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions
from .serializers import WidgetSerializer
from .models import Widget
from widget_project.permissions import AllModelPermission

class WidgetViewSet(viewsets.ModelViewSet):
    """A simple model viewset. By default provides GET, PUT and DELETE requests (delete requires the addition of the object ID to the URL path)

    """
    serializer_class = WidgetSerializer
    queryset = Widget.objects.all()
    permission_classes = [AllModelPermission]
