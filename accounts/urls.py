
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('logout/',views.LogOut,name="logout"),
    path('login/',views.LogIn,name="login"),
]
