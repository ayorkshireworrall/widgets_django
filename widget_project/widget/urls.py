from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/widgets/', views.WidgetListCreate.as_view()),
    path('api/v2/widgets/', views.widget_list),
    path('api/v2/widgets/<int:pk>', views.widget_detail),
]