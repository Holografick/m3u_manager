from django.urls import path
from . import views

urlpatterns = [
    path('ext3mu/', views.all_ext3mu),
]
