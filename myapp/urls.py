from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('add_task/', views.add_task, name = "add_task"),
]
