from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
            path('api_test/', views.api_test, name = 'api_test'),
            path('upload/', views.ImageViewSet.as_view(), name='upload'),
            path('delete/', views.delete_image, name='delete'),
        ]