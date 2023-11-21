from . import views
from django.urls import path

urlpatterns = [
    path("post/", views.post_handler, name="post_handler"),
    path("post/<int:post_id>", views.get_post, name="get_post"),
]
