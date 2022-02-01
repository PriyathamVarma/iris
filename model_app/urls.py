from django.urls import path
from django.conf.urls import include
from model_app import views

# add url functions here for views
urlpatterns = [
    
    path('',views.predictor,name="prediction"),
    
]