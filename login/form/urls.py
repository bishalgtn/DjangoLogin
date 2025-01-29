from django.urls import path
from . import views

urlpatterns = [
    path('', views.form),
    path('form/<slug:slug>/courses/',)
]
