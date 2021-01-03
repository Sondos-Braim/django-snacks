from django.urls import path,include 
from .views import home_view,about_view

urlpatterns = [
    path('', home_view.as_view(),name='home'),
    path('about/', about_view.as_view(),name='about'),
    
]
