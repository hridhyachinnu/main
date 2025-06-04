from django.urls import path
from . import views

urlpatterns = [
    path('', views.intern_feedback_view, name='intern_feedback'),
]
