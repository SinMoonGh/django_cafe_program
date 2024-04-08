from django.urls import path, re_path
from . import views

app_name = "description"
urlpatterns = [
    path('lion/', views.InnovationLionView.as_view(), name='lion_des'),
    path('tiger/', views.InnovationTigerView.as_view(), name='tiger_des'),
]