from django.urls import path
from . import views

urlpatterns = [
    path('', views.control_view, name='control'),
    path('panel/', views.panel_view, name='panel'),
]