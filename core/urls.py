from django.urls import path
from .views import StateAPIView, StateByIdApiView, CityAPIView, CityByIdAPIView

urlpatterns = [
    path('states', StateAPIView.as_view()),
    path('state/<int:pk>', StateByIdApiView.as_view()),
    path('cities',  CityAPIView.as_view()),
    path('city/<int:pk>',  CityByIdAPIView.as_view()),
]
