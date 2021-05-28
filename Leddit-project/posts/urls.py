from django.urls import path
from .views import PostLists, VoteCreate

urlpatterns = [
    path('', PostLists.as_view()),
    path('/<int:pk>/vote/', VoteCreate.as_view())
]