from django.urls import path
from . import views
from .api import WidgetViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v3/widgets', WidgetViewSet, 'widgets')

urlpatterns = [
    path('api/v1/widgets/', views.WidgetListCreate.as_view()),
    path('api/v2/widgets/', views.widget_list),
    path('api/v2/widgets/create', views.add_widget),
    path('api/v2/widgets/<int:pk>', views.widget_detail),
] + router.urls