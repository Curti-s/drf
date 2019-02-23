from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetList, SnippetDetails, UserList, UserDetail, api_root, SnippetHighlight

urlpatterns = [
    path('', api_root),
    path('snippet/', SnippetList.as_view(), name='snippet-list'),
    path('snippet<int:pk>/', SnippetDetails.as_view(), name='snippet-detail'),
    path('snippet/<int:pk>/highlight/',SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users<int:pk>/', UserDetail.as_view(), name='user-deatil'),
]

urlpatterns = format_suffix_patterns(urlpatterns)