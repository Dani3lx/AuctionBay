from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("details/<str:item>/", views.details, name="details"),
    path("add/<str:item>/", views.add, name="add"),
    # path("remove", views.remove, name="remove"),
]
