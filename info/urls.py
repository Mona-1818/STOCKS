from django.urls import path
from . import views

urlpatterns = [
    # path('fillstock/', views.fillstock),
    # path('remove/', views.remove)
    path('allstocks/', views.Allstock),
    # path('personal-recommendation/<str:username>/', views.Personal_recommend),
]