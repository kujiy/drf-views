from django.urls import path
from generics_view import views

urlpatterns = [
    path('generics_view/', views.SnippetList.as_view()),
    path('generics_view/<int:pk>/', views.SnippetDetail.as_view()),
]
