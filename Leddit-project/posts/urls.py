from django.urls import path
from .views import PostLists

urlpatterns = [
    path('', PostLists.as_view()),
]