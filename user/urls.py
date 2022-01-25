from django.urls import path, include

from user import views

urlpatterns = [
    path('users/<slug:id>/', views.UserDetails.as_view()),
]
