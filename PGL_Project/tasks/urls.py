from django.urls import path

from. import views
urlpatterns = [
    path("index", views.index, name="index"),
    path("square", views.square, name="square"),
    path("rectangle", views.rectangle, name="rectangle"),
    path("triangle", views.triangle, name="triangle"),
    path("circle", views.circle, name="circle"),
    path("", views.start, name="Start")
]