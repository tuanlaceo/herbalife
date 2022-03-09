from django.urls import path # nhap duong dan

from . import views  # . nghia la dang o trong cung folder pages

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),   
    path('dashboard', views.dashboard, name='dashboard'), 
]
