from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("<int:post_id>", views.post_comments),
    path("<int:post_id>/upvote", views.upvote_post),
]
