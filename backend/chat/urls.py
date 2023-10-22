from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:slug>", views.DetailView.as_view(), name="detail")
]
