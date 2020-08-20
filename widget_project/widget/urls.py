from django.urls import path
from . import views

urlpatterns = [
    path('api/widgets/', views.WidgetListCreate.as_view()),
]