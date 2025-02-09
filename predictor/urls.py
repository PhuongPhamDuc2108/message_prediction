from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Thêm view 'home'
    path('predict/', views.predict_words, name='predict_words'),  # Thêm view 'predict_words'
]
