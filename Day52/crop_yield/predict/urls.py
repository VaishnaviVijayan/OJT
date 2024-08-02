from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_yield, name='predict_yield'),
]
