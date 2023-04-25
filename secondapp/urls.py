from django.urls import path
from . import views #현재위치의 viwes.py 가져오기

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('army_shop/', views.army_shop),
    
]