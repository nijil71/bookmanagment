from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('register/',register.as_view(),name='register'),
    path('login/',login.as_view(),name='login'),
    path('addbook/',addbook.as_view(),name='addbook'),
    path('deletebook/<pk>/',deletebook.as_view(),name='deletebook'),
    path('updatebook/<pk>/',updatebook.as_view(),name='updatebook'),
    path('download/',download.as_view(),name='download'),
    path('logout/',customlogoutview.as_view(),name='logout'),
]