from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetails, UserList, UserDetail

urlpatterns = [
    path('', SnippetList.as_view()),
    path('<int:pk>/', SnippetDetails.as_view()),
    path('users/', UserList.as_view()),
    path('users<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)