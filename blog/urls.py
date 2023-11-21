from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    # path("post/", views.get_all_posts, name="get_all_posts"),
    # path("post/", views.add_post, name="add_post"),
    path("post/", views.post_handler, name="post_handler"),
    path("post/<int:post_id>", views.get_post, name="get_post"),
]
