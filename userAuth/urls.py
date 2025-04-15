from django.urls import path
from userAuth import views

app_name = 'userAuth'

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),

    path('logout_user/', views.logout_user, name='logout_user'),
]