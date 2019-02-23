from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetails, UserList, UserDetail, api_root, SnippetHighlight

urlpatterns = [
    path('', api_root),
    path('snippet/', SnippetList.as_view()),
    path('snippet<int:pk>/', SnippetDetails.as_view()),
    path('snippet/<int:pk>/highlight/',SnippetHighlight.as_view()),
    path('users/', UserList.as_view()),
    path('users<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)