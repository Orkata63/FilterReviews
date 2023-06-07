from django.urls import path

from . import views

urlpatterns = [
    path("", views.form, name="form"),
    path("filter/", views.filter_reviews, name="filter_reviews")
]