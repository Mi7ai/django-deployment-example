from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('special/',views.special,name='special'),
]
