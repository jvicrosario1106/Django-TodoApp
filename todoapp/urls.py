from django.urls import path
from . import views


urlpatterns = [

    path('', views.home , name = 'home'),
    path('remove/<str:pk>/', views.remove , name = 'remove'),
    path('update/<str:pk>/', views.update , name = 'update'),

]