from django.urls import path

from blog.views import PostListView, PostDetailView, CommentaryCreateView


urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    )
]

app_name = "blog"
