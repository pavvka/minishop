from django.urls import path, include

from user import views

urlpatterns = [
    path('users/<slug:id>/', views.UserDetails.as_view()),
    path('update_profile/<int:pk>/', views.UpdateProfileView.as_view(), name='auth_update_profile')
]
