from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('predict/', views.predict_words, name='predict_words'), 
]
