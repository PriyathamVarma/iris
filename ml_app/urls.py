from django.urls import path
from django.conf.urls import include
from ml_app import views

# add url functions here for views
urlpatterns = [
    path('',views.hello_world),
]