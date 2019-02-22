from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import snippet_list, snippet_details

urlpatterns = [
    path('', snippet_list),
    path('<int:pk>/', snippet_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)