from django.urls import path
from rest_api import views


urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
]
