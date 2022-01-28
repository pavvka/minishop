from django.urls import path, include

from comments import views

urlpatterns = [
    path('products/<slug:product_slug>/', views.CommentList.as_view()),
]