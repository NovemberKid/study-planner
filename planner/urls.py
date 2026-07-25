
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.all_planner, name='all_planner'),
    
]