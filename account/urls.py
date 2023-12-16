from django.urls import path
from . import views

from .views import register_user, user_login, user_logout

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('create_profile/<str:username>/', views.create_user),
    path('update_profile/<str:username>/', views.update_user),
    path('add-protfolio/<str:username>/', views.add_Portfolio),
]