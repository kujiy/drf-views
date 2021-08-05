from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from views_apiview import views

urlpatterns = [
    path('views_apiview/', views.SnippetList.as_view()),
    path('views_apiview/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)