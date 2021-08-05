from django.urls import path
from decorator_view import views

urlpatterns = [
    path('decorator_view/', views.snippet_list),
    path('decorator_view/<int:pk>/', views.snippet_detail),
]
