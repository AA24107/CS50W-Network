
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new_post, name="new_post"),
    path("following", views.following, name="following"),
    path("<str:username>", views.profile, name="profile"),
    path("posts/<int:post_id>", views.post, name="post"),
]
