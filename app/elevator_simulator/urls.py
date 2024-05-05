from django.urls import path
from . import views

urlpatterns = [
    path("hello_world/", views.hello, name='hello'),
    path("status/", views.status, name='status'),
    path("up/", views.up, name='up'),
    path("down/", views.down, name='down'),
    path("select/", views.select, name='select'),
]
