from django.urls import path
from app_cadastro import views
urlpatterns = [
    path('',views.home, name='home')]
