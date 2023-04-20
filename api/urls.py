from django.urls import path

from .views import LoginView, PostListView, PostCreateView, PostUpdateView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('posts/', PostListView.as_view()),
    path('posts/create/', PostCreateView.as_view()),
    path('posts/<int:pk>/update/', PostUpdateView.as_view()),
]
