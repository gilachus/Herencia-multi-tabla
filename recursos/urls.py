from django.urls import path
from .views import video_detail, articulo_detail

urlpatterns = [
    path('artìculo/<int:id>/', articulo_detail),
    path('video/<int:id>/', video_detail)
]