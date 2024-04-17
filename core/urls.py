from django.urls import path
from .views import StateAPIView, StateByIdApiView, CityAPIView

urlpatterns = [
    path('states', StateAPIView.as_view()),
    path('state/<int:pk>', StateByIdApiView.as_view()),
    path('cities',  CityAPIView.as_view()),
]
