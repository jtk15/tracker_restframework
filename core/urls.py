from django.urls import path
from .views import StateAPIView

urlpatterns = [
    path('state', StateAPIView.as_view())
]
