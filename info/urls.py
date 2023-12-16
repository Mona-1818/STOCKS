from django.urls import path
from . import views

urlpatterns = [
    # path('fillstock/', views.fillstock),
    # path('remove/', views.remove)
    path('allstocks/', views.Allstock),
    path('user-portfolio/<str:username>/', views.User_portfolio),
    path('personal-recommendation/<str:username>/', views.Personal_recommend),
]