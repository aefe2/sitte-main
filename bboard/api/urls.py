from django.urls import path
from .views import bbs, BbDetailView
from .views import comments

urlpatterns = [
    path('bbs/<int:pk>/comments/', comments),
    path('bbs/', bbs),
    path('bbs/<int:pk>/', BbDetailView.as_view()),
    path('bbs/', bbs),
]
