from django.urls import path
from . import views

urlpatterns = [
    path('course/<int:course_id>/', views.course, name='course'),
    path('', views.index, name='index'),
]
