from django.urls import path
from . import views

urlpatterns = [
    path('', views.SmsAuthView.as_view({'get': 'get', 'post': 'post'})),
]