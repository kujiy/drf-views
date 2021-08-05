from django.urls import path
from decorator_view import views

urlpatterns = [
    path('generics_view/', views.snippet_list),
    path('generics_view/<int:pk>/', views.snippet_detail),
]
