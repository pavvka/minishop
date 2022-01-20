from django.urls import path, include

from user import views

urlpatterns = [
    path('users/', views.UserDetails.as_view()),
]