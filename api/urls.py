from django.urls import include, path
from . import views

urlpatterns = [
  path('num_to_english', views.number)
]
